# /home/competitor/set_hostname_via_restconf.py
import requests
import sys
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if len(sys.argv) != 3:
   print(f"Usage: {sys.argv[0]} <router_ip> <hostname>")
   sys.exit(1)

router_ip = sys.argv[1]
hostname = sys.argv[2]

headers = {
   "Accept": "application/yang-data+json",
   "Content-type": "application/yang-data+json"
}

url = f"https://{router_ip}/restconf/data/ietf-system:system"

payload = {
   "ietf-system:system": {
       "hostname": hostname
   }
}

response = requests.put(url, headers=headers, json=payload, verify=False, auth=("admin", "admin"))

if response.status_code == 204:
   print(f"Hostname updated to '{hostname}' on router {router_ip}")
else:
   print(f"Error: {response.status_code} - {response.text}")
