import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import Netmiko

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
       
        output = net_connect.send_config_set(loopback_config.split('\n'))
        print("Pushed config to host")

        net_connect.disconnect()
        print("Disconnected from host")

    except Exception as e:
        print("Failed to configure host" )

print("Configuration completed!")