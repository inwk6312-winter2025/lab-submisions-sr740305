from netmiko import Netmiko
import yaml
import logging

# Configure logging
logging.basicConfig(filename='routing_table.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load host information
hosts = yaml.load(open('Exercise1_hosts.yml'), Loader=yaml.SafeLoader)

# Collect routing tables
for host in hosts['hosts']:
    try:
        net_connect = Netmiko(host=host['name'],
                              username=host['username'],
                              password=host['password'],
                              port=host['port'],
                              device_type=host['type'])
        logging.info(f"Connected to {host['name']}")

        output = net_connect.send_command("show ip route", use_textfsm=True)
        logging.info(f"Routing table for {host['name']}: {output}")

        net_connect.disconnect()
        logging.info(f"Disconnected from {host['name']}")

    except Exception as e:
        logging.error(f"Failed to retrieve routing table from {host['name']}: {e}")

print("Routing table collection completed!")