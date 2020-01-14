#!/usr/bin/python3
"""
script that takes in a string and sends
a search request to the Star Wars API
"""
from sys import argv
import requests

url = "https://swapi.co/api/people/?search={}".format(argv[1])
req = requests.get(url).json()
print("Number of results: {}".format(req['count']))
for data in req['results']:
    print("{}".format(data['name']))
