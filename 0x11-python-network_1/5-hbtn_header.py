#!/usr/bin/python3
# Script that fetches an URL using requests
import requests
from sys import argv
if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io')
    print(req.headers.get('X-Request-Id'))
