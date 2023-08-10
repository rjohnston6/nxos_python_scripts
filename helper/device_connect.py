import logging
import json
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException

log = logging.getLogger(__name__)


def query_device(device):
    """
    This function connects to received device and gathers the oprhan ports
    and the hostname for the device and writes to output file.
    """

    orphan_ports = []

    try:
        net_connect = ConnectHandler(**device)
        logging.info(f"Connected from {device['host']}")

        hostname = net_connect.send_command("show hostname")
        output = net_connect.send_command("show vpc orphan-port | json")

        if "Note" in output:
            result = {
                "hostname": hostname.split()[0],
                "mgmt_ip": device["host"],
                "vpc_vlan": "N/A",
                "orphan_ports": "None Found",
            }
            orphan_ports.append(result)

        else:
            joutput = json.loads(output)
            orphan_table = joutput["TABLE_orphan_ports"]["ROW_orphan_ports"]

            if isinstance(orphan_table, list):
                for row in orphan_table:
                    result = {
                        "hostname": hostname.split()[0],
                        "mgmt_ip": device["host"],
                        "vpc_vlan": row["vpc-vlan"],
                        "orphan_ports": row["vpc-orphan-ports"],
                    }

                    logging.info(result)
                    orphan_ports.append(result)
            else:
                result = {
                    "hostname": hostname.split()[0],
                    "mgmt_ip": device["host"],
                    "vpc_vlan": orphan_table["vpc-vlan"],
                    "orphan_ports": orphan_table["vpc-orphan-ports"],
                }

                logging.info(result)
                orphan_ports.append(result)

            net_connect.disconnect()
            logging.info(f"Disconnected from {device['host']}")
        return orphan_ports

    except NetmikoAuthenticationException as ex:
        logging.error(
            f"Authentication issue connecting to {device['host']}, device skipped!"
        )
        result = {
            "hostname": "AuthenticationError",
            "mgmt_ip": device["host"],
            "vpc_vlan": "Unknown",
            "orphan_ports": "Unknown",
        }
        orphan_ports.append(result)

    except NetmikoTimeoutException as ex:
        logging.error(f"Connection Timed out for {device['host']}, device skipped!")
        result = {
            "hostname": "ConnectionError",
            "mgmt_ip": device["host"],
            "vpc_vlan": "Unknown",
            "orphan_ports": "Unknown",
        }
        orphan_ports.append(result)
        return orphan_ports

    except Exception as ex:
        print("-" * 80)
        print(ex)
        print("-" * 80)
