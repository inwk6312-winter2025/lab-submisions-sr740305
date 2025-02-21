from netmiko import Netmiko
devices = [{"device_type": "cisco_ios",
            "ip": "192.168.1.101",
            "username": "student",
            "password": "Meilab123",
            "port": "22",}]
description = 'Loopback Interface'
description_config = ["interface loopback0", "ip address 150.1.1.1 255.255.255.255",
                      f"description {description}", "no shut"]

for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_config_set(description_config)
    print(output)
    net_connect.disconnect()