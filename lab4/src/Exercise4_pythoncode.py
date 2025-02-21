import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import Netmiko
import logging

# Configure logging
logging.basicConfig(filename='network_config.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load YAML files
hosts = yaml.load(open('Exercise1_hosts.yml'), Loader=yaml.SafeLoader)
interfaces = yaml.load(open('Exercise1_interfaces.yml'), Loader=yaml.SafeLoader)

# Load Jinja2 template
env = Environment(loader=FileSystemLoader('.'), trim_blocks=True, autoescape=True)
template = env.get_template('Exercise2_config_template.j2')
loopback_config = template.render(data=interfaces)

# Deploy configuration to devices
for host in hosts['hosts']:
    try:
        net_connect = Netmiko(host=host['name'],
                              username=host['username'],
                              password=host['password'],
                              port=host['port'],
                              device_type=host['type'])
        logging.info(f"Logged into {host['name']} successfully")

        output = net_connect.send_config_set(loopback_config.split('\n'))
        logging.info(f"Pushed config to {host['name']} successfully: {output}")

        net_connect.disconnect()
        logging.info(f"Disconnected from {host['name']}")

    except Exception as e:
        logging.error(f"Failed to configure {host['name']}: {e}")

print("Configuration completed!")