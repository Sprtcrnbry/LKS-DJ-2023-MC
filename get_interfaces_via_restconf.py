# /home/competitor/get_interfaces_via_restconf.py
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

# Adjusted URL and payload based on example documentation
url = f"https://{router_ip}/restconf/data/Cisco-IOS-XE-native:native/hostname"

payload = {
    "Cisco-IOS-XE-native:hostname": hostname
}

print(f"Request URL: {url}")
print(f"Payload: {payload}")

response = requests.put(url, headers=headers, json=payload, verify=False, auth=("admin", "admin"))

print(f"Response Code: {response.status_code}")
print(f"Response Text: {response.text}")

if response.status_code == 204:
   print(f"Hostname updated to '{hostname}' on router {router_ip}")
else:
   print(f"Error: {response.status_code} - {response.text}")
