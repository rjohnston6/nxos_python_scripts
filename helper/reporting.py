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

        for rows in data:
            for row in rows:
                writer.writerow(row)
