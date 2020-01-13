#!/usr/bin/python3
# Script that fetches an URL using requests
import requests
from sys import argv
req = requests.get('https://intranet.hbtn.io/status')
print(req.headers['X-Request-Id'])
