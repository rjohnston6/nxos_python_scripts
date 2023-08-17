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
import json
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException

log = logging.getLogger(__name__)


def json(device, commands):
    """
    This function connects to a device gathers the hostname and runs the
    provided commands then returns a dictionary
    {hostname: {command1: output, command2: output}}
    """

    output = {}

    try:
        net_connect = ConnectHandler(**device)
        logging.info(f"Connected from {device['host']}")

        hostname = net_connect.send_command("show hostname")
        hostname = hostname.split()[0]
        output[hostname] = {}

        for command in commands:
            if "json" in command:
                command_out = net_connect.send_command(command)
                output[hostname][command] = command_out

            else:
                logging.info(
                    f"Expecting a JSON based command, recieved: {command}, skipped"
                )

        net_connect.disconnect()
        logging.info(f"Disconnected from {device['host']}")
        return output

    except NetmikoAuthenticationException as ex:
        logging.error(
            f"Authentication issue connecting to {device['host']}, device skipped!"
        )
        output[device["host"]] = "AuthenticationError"
        return output

    except NetmikoTimeoutException as ex:
        logging.error(f"Connection Timed out for {device['host']}, device skipped!")
        output[device["host"]] = "ConnectionTimeOut"
        return output

    except Exception as ex:
        print("-" * 80)
        print(ex)
        print("-" * 80)


# def query_device(device):
#     """
#     This function connects to received device and gathers the oprhan ports
#     and the hostname for the device and writes to output file.
#     """

#     orphan_ports = []

#     try:
#         net_connect = ConnectHandler(**device)
#         logging.info(f"Connected from {device['host']}")

#         hostname = net_connect.send_command("show hostname")
#         output = net_connect.send_command("show vpc orphan-port | json")

#         if "Note" in output:
#             result = {
#                 "hostname": hostname.split()[0],
#                 "mgmt_ip": device["host"],
#                 "vpc_vlan": "N/A",
#                 "orphan_ports": "None Found",
#             }
#             orphan_ports.append(result)

#         else:
#             joutput = json.loads(output)
#             orphan_table = joutput["TABLE_orphan_ports"]["ROW_orphan_ports"]

#             if isinstance(orphan_table, list):
#                 for row in orphan_table:
#                     result = {
#                         "hostname": hostname.split()[0],
#                         "mgmt_ip": device["host"],
#                         "vpc_vlan": row["vpc-vlan"],
#                         "orphan_ports": row["vpc-orphan-ports"],
#                     }

#                     logging.info(result)
#                     orphan_ports.append(result)
#             else:
#                 result = {
#                     "hostname": hostname.split()[0],
#                     "mgmt_ip": device["host"],
#                     "vpc_vlan": orphan_table["vpc-vlan"],
#                     "orphan_ports": orphan_table["vpc-orphan-ports"],
#                 }

#                 logging.info(result)
#                 orphan_ports.append(result)

#             net_connect.disconnect()
#             logging.info(f"Disconnected from {device['host']}")
#         return orphan_ports

#     except NetmikoAuthenticationException as ex:
#         logging.error(
#             f"Authentication issue connecting to {device['host']}, device skipped!"
#         )
#         result = {
#             "hostname": "AuthenticationError",
#             "mgmt_ip": device["host"],
#             "vpc_vlan": "Unknown",
#             "orphan_ports": "Unknown",
#         }
#         orphan_ports.append(result)

#     except NetmikoTimeoutException as ex:
#         logging.error(f"Connection Timed out for {device['host']}, device skipped!")
#         result = {
#             "hostname": "ConnectionError",
#             "mgmt_ip": device["host"],
#             "vpc_vlan": "Unknown",
#             "orphan_ports": "Unknown",
#         }
#         orphan_ports.append(result)
#         return orphan_ports

#     except Exception as ex:
#         print("-" * 80)
#         print(ex)
#         print("-" * 80)
