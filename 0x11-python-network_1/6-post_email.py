#!/usr/bin/python3
# Script that fetches an URL using requests
import requests
from sys import argv
if __name__ == "__main__":
    file = {'email': argv[2]}
    req = requests.post(argv[1], file)
    print(req.content.decode('utf-8'))