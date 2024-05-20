# /home/competitor/get_interfaces_via_restconf.py
import requests
import sys
import json
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <router_ip>")
    sys.exit(1)

router_ip = sys.argv[1]

headers = {
    "Accept": "application/yang-data+json"
}

url = f"https://{router_ip}/restconf/data/ietf-interfaces:interfaces"

response = requests.get(url, headers=headers, verify=False, auth=("admin", "admin"))

if response.status_code == 200:
    interfaces = response.json()["ietf-interfaces:interfaces"]["interface"]
    filtered_interfaces = [
        {
            "interface": iface["name"],
            "ip": iface["ietf-ip:ipv4"]["address"][0]["ip"] if "ietf-ip:ipv4" in iface and iface["ietf-ip:ipv4"] and "address" in iface["ietf-ip:ipv4"] and iface["ietf-ip:ipv4"]["address"] else None
        }
        for iface in interfaces
    ]
    filtered_interfaces = [iface for iface in filtered_interfaces if iface["ip"] is not None]
    output = {"interfaces": filtered_interfaces}
    print(json.dumps(output, indent=4))
else:
    print(f"Error: {response.status_code} - {response.text}")
