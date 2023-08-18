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


def json_cmd(device, commands):
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
        output[hostname]["mgmt-ip"] = device["host"]

        for command in commands:
            if "json" in command:
                command_out = net_connect.send_command(command)
                if "Note" not in command_out:
                    output[hostname][command] = json.loads(command_out)
                else:
                    output[hostname][command] = "Empty JSON"

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
