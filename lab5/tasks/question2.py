import yaml
import requests
from requests.auth import HTTPBasicAuth
import json

# Load YAML configuration
with open("question1.yaml", "r") as file:
    routers = yaml.safe_load(file)["routers"]

# RESTCONF authentication
USER = "student"
PASS = "Meilab123"
HEADERS = {
    "Accept": "application/vnd.yang.data+json",
    "Content-Type": "application/vnd.yang.data+json"
}

def configure_interface(router, interface, ip):
    url = f"http://{routers[router]['management_ip']}/restconf/api/running/interfaces/interface/{interface}"
    data = {
        "ietf-interfaces:interface": {
            "name": interface,
            "description": "Configured via RESTCONF",
            "type": "iana-if-type:ethernetCsmacd",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [{
                    "ip": ip,
                    "netmask": "255.255.255.0"
                }]
            },
            "ietf-ip:ipv6": {}
        }
    }
    response = requests.put(url, auth=HTTPBasicAuth(USER, PASS), headers=HEADERS, data=json.dumps(data))
    if response.status_code == 204:
        print(f"Successfully configured {interface} on {router}")
    else:
        print(f"Failed to configure {interface} on {router}: {response.text}")

# Apply configurations to all routers
for router, details in routers.items():
    for interface, ip in details["interfaces"].items():
        configure_interface(router, interface, ip)
