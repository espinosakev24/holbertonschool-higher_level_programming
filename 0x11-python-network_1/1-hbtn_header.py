#!/usr/bin/python3
# Script that displays the value of the X-Request-Id variable from header
import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.info().get('X-Request-Id'))
