#!/usr/bin/python3
"""
script that takes your Github credentials
(username and password) and uses the Github
API to display your id
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = "https://api.github.com/users"
    username = argv[1]
    password = argv[2]
    req = requests.get(url, auth=(username, password))
    if "id" in req.json():
        print(req.json().get('id'))
    else:
        print(None)
