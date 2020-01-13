#!/usr/bin/python3
"""
takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    data = {'q': q}
    url = "http://0.0.0.0:5000/search_user"
    req = requests.post(url, data)
    try:
        req_dict = req.json()
        if (len(req_dict) == 0):
            print("No result")
        else:
            print("[{}] {}".format(req_dict.get('id'), req_dict.get('name')))
    except Exception:
            print("Not a valid JSON")
