#!/usr/bin/python3
"""
Script that displays the value of the X-Request-Id
"""
import urllib.parse
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
