import logging
from rich.prompt import Prompt

log = logging.getLogger(__name__)


def get_credentials():
    """
    This funciton ask for User and Password for the devices.
    """

    user = Prompt.ask(f"Enter Username for Device Connectivity: ")
    pwd = Prompt.ask(f"Enter Password for Device Connectivity: ", password=True)

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
