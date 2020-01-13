#!/usr/bin/python3
"""
script that takes in a string and sends
a search request to the Star Wars API
"""
from sys import argv
import requests


req = requests.get("https://swapi.co/api/people/?search={}".format(argv[1]))
req_json = req.json()
print("Number of results: {}".format(req_json['count']))
for data in req_json['results']:
    print("{}".format(data['name']))
