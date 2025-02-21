from netmiko import Netmiko

r1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101", # R1 Mgmt Interface
    "username": "student",
    "password": "Meilab123",
    "secret": "cisco",
    "port": "22",
    }

r2 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.102", # R2 Mgmt Interface
    "username": "student",
    "password": "Meilab123",
    "secret": "cisco",
    "port": "22",
    }

r3 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.103", # R3 Mgmt Interface
    "username": "student",
    "password": "Meilab123",
    "secret": "cisco",
    "port": "22",
    }

for device in (r1, r2, r3):
    net_connect = Netmiko(**device)
    print(f"Default prompt: {net_connect.find_prompt()}")
    
    net_connect.send_command_timing("disable")
    print(f"Disable command: {net_connect.find_prompt()}")
    
    net_connect.enable()
    print(f"Enable command: {net_connect.find_prompt()}")