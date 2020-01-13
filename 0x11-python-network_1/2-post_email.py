#!/usr/bin/python3
"""
Script that sends a POST request to the-
passed URL with the email as a parameter.
"""
import urllib.parse
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
