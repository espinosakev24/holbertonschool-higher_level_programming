#!/usr/bin/python3
# Script that fetches an URL
import urllib.request

print("Body response:")
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    body = response.read()
    print("\t- type: {}".format(type(response.read())))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
    response.close()
