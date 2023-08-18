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
import csv

from rich.table import Table

log = logging.getLogger(__name__)


def terminal_table_report(tbl_name, columns):
    table = Table(title=tbl_name, show_lines=True)
    for column in columns:
        table.add_column(column, justify="Left", style="cyan", no_wrap=True)

    return table


def csv_report(headers, output_file, data):
    file = open(output_file, "w", newline="")
    with file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

        for row in data:
            writer.writerow(row)

    file.close()
