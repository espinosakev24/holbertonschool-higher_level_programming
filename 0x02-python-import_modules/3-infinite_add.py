#!/usr/bin/python3
from sys import argv
if len(argv) > 0:
    print(sum(map(int, argv[1:])))
