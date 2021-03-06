#!/usr/bin/python3
"""
script that takes your Github credentials
(username and password) and uses the Github
API to display your id.
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = argv[1]
    password = argv[2]
    try:
        req = requests.get(url, auth=(username, password))
        print(req.json().get('id'))
    except Exception:
        print(None)
