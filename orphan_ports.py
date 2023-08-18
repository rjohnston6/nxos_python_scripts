#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""NXOS Python Scripts.

Copyright (c) 2023 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Russell Johnston"
__email__ = "rujohns2@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2023 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"
__credits__ = ["Juan Andres Rocha Bravo"]

import logging
import argparse
import multiprocessing

from datetime import datetime
from rich.logging import RichHandler
from rich.console import Console

from helper import devices, reporting
from helper import query_device

FORMAT = "%(message)s"
logging.basicConfig(
    level=logging.DEBUG, format=FORMAT, datefmt="[%X]", handlers=[RichHandler]
)

log = logging.getLogger(__name__)

console = Console()


def run_commands(device, commands, mpQueue):
    """
    This is a wraper of the run_commands function.Original function returns
    a tuple with the device and the Authentication Exception
    When the function gets the tuple it will extract the device and add it
    to the mpQueue
    """
    result = query_device.json_cmd(device, commands)

    if isinstance(result, tuple):
        mpQueue.put(None)
    else:
        mpQueue.put(result)


def search_neighbors(neighbors, port):
    for neighbor in neighbors:
        if neighbor["l_port_id"] == port:
            return neighbor


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Connects to the Nexus switches listed on the hosts file, "
        "gets the output of the commands listed on the commands file and save "
        "them on a new file"
    )

    # requiredNamed = parser.add_argument_group("required named arguments")

    parser.add_argument(
        "-d",
        "--devices",
        help="File containing the switches to connect",
        required=False,
        default="devices.txt",
    )

    parser.add_argument("-t", "--print_table", required=False, action="store_true")

    parser.add_argument("-r", "--csv_report", required=False, action="store_true")

    args = parser.parse_args()
    devices_file = args.devices

    user, pwd = devices.get_credentials()

    start_time = datetime.now()

    devices = devices.get_devices(devices_file, user, pwd)

    mpQueue = multiprocessing.Queue()
    processes = []
    raw_output = []

    for device in devices:
        """
        Connect to each device in the provided file and query for the
        orphan-ports along with the lldp neighbors and store outputs from to
        raw_output for further data formatting.
        """

        commands = ["show vpc orphan-ports | json", "show lldp neighbors | json"]
        p = multiprocessing.Process(
            target=run_commands, args=(device, commands, mpQueue)
        )

        processes.append(p)
        p.start()

    for p in processes:
        p.join()
        raw_output.append(mpQueue.get())

    output = []
    for switch in raw_output:
        """
        Take each switches output and format the data as preferred outputting
        to a dictionary in the following format:
        { hostname: 'hostname',
          mgmt-ip: 'mgmt-ip'
          vpc-vlan: 'vpc-vlan',
          orphan-port: 'port',
          lldp-neighbor: 'neigbour',
          lldp-neighbor-mgmt-ip: 'neighbor-ip',
        }
        Each dictionary will be added to the output list var for display
        in tables and csv report as determined by cli flags (-t and/or -r).
        """
        for k, v in switch.items():
            ip_addr = v["mgmt-ip"]
            neighbors = v["show lldp neighbors | json"]["TABLE_nbor"]["ROW_nbor"]
            if "Empty JSON" not in v["show vpc orphan-ports | json"]:
                if isinstance(
                    v["show vpc orphan-ports | json"]["TABLE_orphan_ports"][
                        "ROW_orphan_ports"
                    ],
                    list,
                ):
                    for vlan in v["show vpc orphan-ports | json"]["TABLE_orphan_ports"][
                        "ROW_orphan_ports"
                    ]:
                        ports = [x.strip() for x in vlan["vpc-orphan-ports"].split(",")]
                        for port in ports:
                            neighbor = search_neighbors(neighbors, port)
                            data = {
                                "hostname": k,
                                "mgmt-ip": ip_addr,
                                "vpc-vlan": vlan["vpc-vlan"],
                                "orphan-port": port,
                            }
                            if neighbor is None:
                                data["lldp-neighbor"] = ""
                                data["lldp-neighbor-mgmt-ip"] = ""
                            else:
                                data["lldp-neighbor"] = neighbor["chassis_id"]
                                data["lldp-neighbor-mgmt-ip"] = neighbor["mgmt_addr"]
                            output.append(data)
                else:
                    ports = v["show vpc orphan-ports | json"]["TABLE_orphan_ports"][
                        "ROW_orphan_ports"
                    ]["vpc-orphan-ports"].split(",")
                    for port in ports:
                        neighbor = search_neighbors(neighbors, port)
                        data = {
                            "hostname": k,
                            "mgmt-ip": ip_addr,
                            "vpc-vlan": v["show vpc orphan-ports | json"][
                                "TABLE_orphan_ports"
                            ]["ROW_orphan_ports"]["vpc-vlan"],
                            "orphan-port": port,
                        }
                        if neighbor is None:
                            data["lldp-neighbor"] = ""
                            data["lldp-neighbor-mgmt-ip"] = ""
                        else:
                            data["lldp-neighbor"] = neighbor["chassis_id"]
                            data["lldp-neighbor-mgmt-ip"] = neighbor["mgmt_addr"]
                        output.append(data)
            else:
                # Handle Switches with no Orphan Ports
                data = {
                    "hostname": k,
                    "mgmt-ip": ip_addr,
                    "vpc-vlan": "N/A",
                    "orphan-port": "None Found",
                    "lldp-neighbor": "",
                    "lldp-neighbor-mgmt-ip": "",
                }
                output.append(data)

    if args.csv_report:
        d = datetime.now()
        csv_headers = [
            "hostname",
            "mgmt-ip",
            "vpc-vlan",
            "orphan-port",
            "lldp-neighbor",
            "lldp-neighbor-mgmt-ip",
        ]
        # Generate csv report with included date and time of creation.
        reporting.csv_report(
            csv_headers, f"orphan_ports_{d.strftime('%d%m%y_%H%M%S')}.csv", output
        )

    if args.print_table:
        tbl_columns = [
            "Hostname",
            "Management IP",
            "VPC VLAN",
            "Orphan Port",
            "LLDP Neighbor",
            "LLDP Neighbor IP",
        ]
        table = reporting.terminal_table_report("Orphan Ports", tbl_columns)

        for row in output:
            table.add_row(
                row["hostname"],
                row["mgmt-ip"],
                row["vpc-vlan"],
                row["orphan-port"],
                row["lldp-neighbor"],
                row["lldp-neighbor-mgmt-ip"],
            )

        console.print(table)

    finish_time = datetime.now()
    exec_time = (finish_time - start_time).total_seconds()
    logging.info(f"Execution time: {exec_time:} ms")
