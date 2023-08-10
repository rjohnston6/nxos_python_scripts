#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""NXOS Python Scripts Console Script.

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

import logging
import argparse
import multiprocessing

from datetime import datetime
from rich.logging import RichHandler
from rich.console import Console

from helper import devices, reporting
from helper.device_connect import query_device

__author__ = "Russell Johnston"
__email__ = "rujohns2@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2023 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"
__credits__ = ["Juan Andres Rocha Bravo"]

FORMAT = "%(message)s"
logging.basicConfig(
    level=logging.ERROR, format=FORMAT, datefmt="[%X]", handlers=[RichHandler]
)

log = logging.getLogger(__name__)

console = Console()


def run_command(device, mpQueue):
    """
    This is a wraper of the run_commands function.Original function returns
    a tuple with the device and the Authentication Exception
    When the function gets the tuple it will extract the device and add it
    to the mpQueue
    """
    result = query_device(device)

    if isinstance(result, tuple):
        mpQueue.put(None)
    else:
        mpQueue.put(result)


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
    output = []

    for device in devices:
        p = multiprocessing.Process(target=run_command, args=(device, mpQueue))

        processes.append(p)
        p.start()

    for p in processes:
        p.join()
        output.append(mpQueue.get())

    if args.csv_report:
        csv_headers = ["hostname", "mgmt_ip", "vpc_vlan", "orphan_ports"]
        reporting.csv_report(csv_headers, "orphan_ports.csv", output)

    if args.print_table:
        tbl_columns = ["Hostname", "Management IP", "VPC VLAN", "Orphan Ports"]
        table = reporting.terminal_table_report("Orphan Ports", tbl_columns)

        for row in output:
            for vlan in row:
                table.add_row(
                    vlan["hostname"],
                    vlan["mgmt_ip"],
                    vlan["vpc_vlan"],
                    vlan["orphan_ports"],
                )

        console.print(table)

    finish_time = datetime.now()
    exec_time = (finish_time - start_time).total_seconds()
    logging.info(f"Execution time: {exec_time:} ms")
