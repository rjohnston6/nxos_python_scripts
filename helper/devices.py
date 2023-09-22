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
from rich.prompt import Prompt

log = logging.getLogger(__name__)


def get_credentials():
    """
    This funciton ask for User and Password for the devices.
    """

    user = Prompt.ask(f"Enter Username for Device Connectivity")
    pwd = Prompt.ask(f"Enter Password for Device Connectivity", password=True)

    return (user, pwd)


def get_devices(file, user, pwd):
    """
    This funciton opens a device file and creates a dictionaries list
    with the following format:
        [
            { 'device_type': 'cisco_nxos', 'host': 'XXXX',
                'username': 'XXXX', 'password': 'XXXX' },
            { 'device_type': 'cisco_nxos', 'host': 'XXXX',
                'username': 'XXXX', 'password': 'XXXX' }
        ]
    """

    devices = []

    with open(file, mode="r", encoding="utf-8-sig") as read_file:
        for fileLine in read_file:
            data = fileLine.strip().split(",")
            node = {
                "device_type": "cisco_nxos",
                "host": data[0],
                "username": user,
                "password": pwd,
            }
            devices.append(node)
    return devices
