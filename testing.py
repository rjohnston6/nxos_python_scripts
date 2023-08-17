output = [
    {
        "nxos9000-1": {
            "show vpc orphan-ports | json": "Empty JSON",
            "show lldp neighbors | json": {
                "neigh_hdr": "neigh_hdr",
                "TABLE_nbor": {
                    "ROW_nbor": [
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-0",
                            "l_port_id": "Eth1/1",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/1",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.10",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "5212.a2d0.0101",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-0",
                            "l_port_id": "Eth1/2",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/2",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.10",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "5212.a2d0.0102",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-2",
                            "l_port_id": "Eth1/3",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/4",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.12",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "521d.ed75.0104",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-3",
                            "l_port_id": "Eth1/4",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/4",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.13",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "520f.a44a.0104",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-4",
                            "l_port_id": "Eth1/5",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/4",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.14",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "5208.f02f.0104",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-5",
                            "l_port_id": "Eth1/6",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/4",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.15",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "520f.31fa.0104",
                        },
                    ]
                },
                "neigh_count": "6",
            },
        }
    },
    {
        "nxos9000-4": {
            "show vpc orphan-ports | json": {
                "TABLE_orphan_ports": {
                    "ROW_orphan_ports": [
                        {"vpc-vlan": "10", "vpc-orphan-ports": "Eth1/6"},
                        {"vpc-vlan": "20", "vpc-orphan-ports": "Eth1/7"},
                    ]
                }
            },
            "show lldp neighbors | json": {
                "neigh_hdr": "neigh_hdr",
                "TABLE_nbor": {
                    "ROW_nbor": [
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-5",
                            "l_port_id": "Eth1/1",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/1",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.15",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "520f.31fa.0101",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-5",
                            "l_port_id": "Eth1/2",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/2",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.15",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "520f.31fa.0102",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-0",
                            "l_port_id": "Eth1/3",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/5",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.10",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "5212.a2d0.0105",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-1",
                            "l_port_id": "Eth1/4",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/5",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.11",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "521d.4560.0105",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "server-4",
                            "l_port_id": "Eth1/6",
                            "hold_time": "120",
                            "system_capability": "BWRS",
                            "enabled_capability": "S",
                            "port_type": "Mac Address",
                            "port_id": "5254.0005.1632",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "192.168.10.30",
                            "mgmt_addr_ipv6_type": "IPV6",
                            "mgmt_addr_ipv6": "fe80::5054:ff:fe1d:4288",
                        },
                    ]
                },
                "neigh_count": "5",
            },
        }
    },
    {
        "nxos9000-0": {
            "show vpc orphan-ports | json": "Empty JSON",
            "show lldp neighbors | json": {
                "neigh_hdr": "neigh_hdr",
                "TABLE_nbor": {
                    "ROW_nbor": [
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-1",
                            "l_port_id": "Eth1/1",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/1",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.11",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "521d.4560.0101",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-1",
                            "l_port_id": "Eth1/2",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/2",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.11",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "521d.4560.0102",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-2",
                            "l_port_id": "Eth1/3",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/3",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.12",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "521d.ed75.0103",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-3",
                            "l_port_id": "Eth1/4",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/3",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.13",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "520f.a44a.0103",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-4",
                            "l_port_id": "Eth1/5",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/3",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.14",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "5208.f02f.0103",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-5",
                            "l_port_id": "Eth1/6",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/3",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.15",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "520f.31fa.0103",
                        },
                    ]
                },
                "neigh_count": "6",
            },
        }
    },
    {
        "nxos9000-3": {
            "show vpc orphan-ports | json": {
                "TABLE_orphan_ports": {
                    "ROW_orphan_ports": {"vpc-vlan": "10", "vpc-orphan-ports": "Eth1/6"}
                }
            },
            "show lldp neighbors | json": {
                "neigh_hdr": "neigh_hdr",
                "TABLE_nbor": {
                    "ROW_nbor": [
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-2",
                            "l_port_id": "Eth1/1",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/1",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.12",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "521d.ed75.0101",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-2",
                            "l_port_id": "Eth1/2",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/2",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.12",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "521d.ed75.0102",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-0",
                            "l_port_id": "Eth1/3",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/4",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.10",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "5212.a2d0.0104",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-1",
                            "l_port_id": "Eth1/4",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/4",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.11",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "521d.4560.0104",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "server-3",
                            "l_port_id": "Eth1/6",
                            "hold_time": "120",
                            "system_capability": "BWRS",
                            "enabled_capability": "S",
                            "port_type": "Mac Address",
                            "port_id": "5254.0019.cb6c",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "192.168.10.20",
                            "mgmt_addr_ipv6_type": "IPV6",
                            "mgmt_addr_ipv6": "fe80::5054:ff:fe13:6686",
                        },
                    ]
                },
                "neigh_count": "5",
            },
        }
    },
    {
        "nxos9000-2": {
            "show vpc orphan-ports | json": {
                "TABLE_orphan_ports": {
                    "ROW_orphan_ports": [
                        {"vpc-vlan": "10", "vpc-orphan-ports": "Eth1/6, Eth1/7"},
                        {"vpc-vlan": "20", "vpc-orphan-ports": "Eth1/7"},
                    ]
                }
            },
            "show lldp neighbors | json": {
                "neigh_hdr": "neigh_hdr",
                "TABLE_nbor": {
                    "ROW_nbor": [
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-3",
                            "l_port_id": "Eth1/1",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/1",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.13",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "520f.a44a.0101",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-3",
                            "l_port_id": "Eth1/2",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/2",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.13",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "520f.a44a.0102",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-0",
                            "l_port_id": "Eth1/3",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/3",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.10",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "5212.a2d0.0103",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-1",
                            "l_port_id": "Eth1/4",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/3",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.11",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "521d.4560.0103",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "server-1",
                            "l_port_id": "Eth1/6",
                            "hold_time": "120",
                            "system_capability": "BWRS",
                            "enabled_capability": "S",
                            "port_type": "Mac Address",
                            "port_id": "5254.0016.526a",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "192.168.10.10",
                            "mgmt_addr_ipv6_type": "IPV6",
                            "mgmt_addr_ipv6": "fe80::5054:ff:fe16:526a",
                        },
                    ]
                },
                "neigh_count": "5",
            },
        }
    },
    {
        "nxos9000-5": {
            "show vpc orphan-ports | json": {
                "TABLE_orphan_ports": {
                    "ROW_orphan_ports": {"vpc-vlan": "20", "vpc-orphan-ports": "Eth1/6"}
                }
            },
            "show lldp neighbors | json": {
                "neigh_hdr": "neigh_hdr",
                "TABLE_nbor": {
                    "ROW_nbor": [
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-4",
                            "l_port_id": "Eth1/1",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/1",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.14",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "5208.f02f.0101",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-4",
                            "l_port_id": "Eth1/2",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/2",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.14",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "5208.f02f.0102",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-0",
                            "l_port_id": "Eth1/3",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/6",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.10",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "5212.a2d0.0106",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "nxos9000-1",
                            "l_port_id": "Eth1/4",
                            "hold_time": "120",
                            "system_capability": "BR",
                            "enabled_capability": "BR",
                            "port_type": "Interface Name",
                            "port_id": "Ethernet1/6",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "100.64.1.11",
                            "mgmt_addr_ipv6_type": "802",
                            "mgmt_addr_ipv6": "521d.4560.0106",
                        },
                        {
                            "chassis_type": "Locally Assigned",
                            "chassis_id": "server-5",
                            "l_port_id": "Eth1/6",
                            "hold_time": "120",
                            "system_capability": "BWRS",
                            "enabled_capability": "S",
                            "port_type": "Mac Address",
                            "port_id": "5254.0007.7a00",
                            "mgmt_addr_type": "IPV4",
                            "mgmt_addr": "192.168.20.20",
                            "mgmt_addr_ipv6_type": "IPV6",
                            "mgmt_addr_ipv6": "fe80::5054:ff:fe07:7a00",
                        },
                    ]
                },
                "neigh_count": "5",
            },
        }
    },
]

out = []
for sw in output:
    for k, v in sw.items():
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
                    ports = vlan["vpc-orphan-ports"].split(",")
                    for port in ports:
                        data = {}
                        data["hostname"] = k
                        data["vpc-vlan"] = vlan["vpc-vlan"]
                        data["orphan-port"] = port
                        for neighbor in v["show lldp neighbors | json"]["TABLE_nbor"][
                            "ROW_nbor"
                        ]:
                            if port in neighbor["l_port_id"]:
                                data["lldp-neighbor"] = neighbor["chassis_id"]
                            else:
                                data["lldp-neighbor"] = ""
                        out.append(data)

                    # for port in ports:
                    #     print(f'{k} : vlan: {vlan["vpc-vlan"]} port : {port}')
            else:
                ports = v["show vpc orphan-ports | json"]["TABLE_orphan_ports"][
                    "ROW_orphan_ports"
                ]["vpc-orphan-ports"].split(",")
                for port in ports:
                    data = {}
                    data["hostname"] = k
                    data["vpc-vlan"] = v["show vpc orphan-ports | json"][
                        "TABLE_orphan_ports"
                    ]["ROW_orphan_ports"]["vpc-vlan"]
                    data["orphan-port"] = port
                    for neighbor in v["show lldp neighbors | json"]["TABLE_nbor"][
                        "ROW_nbor"
                    ]:
                        if port in neighbor["l_port_id"]:
                            data["lldp-neighbor"] = neighbor["chassis_id"]
                        else:
                            data["lldp-neighbor"] = ""
                    out.append(data)
for o in out:
    print(o)
