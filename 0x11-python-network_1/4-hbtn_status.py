#!/usr/bin/python3
# Script that fetches an URL using requests
import requests

print("Body response:")
req = requests.get('https://intranet.hbtn.io/status')
print("\t- type: {}".format(type(req.text)))
print("\t- content: {}".format(req.text))
