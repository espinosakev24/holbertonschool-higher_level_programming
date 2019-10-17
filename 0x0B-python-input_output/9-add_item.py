#!/usr/bin/python3
"""Script that adds elements to a list in json notation"""
from sys import argv
from os.path import isfile
arch = "add_item.json"
if not isfile(arch):
    save_to_json_file([], arch)
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
new_list = []
for a in range(1, len(argv)):
    new_list.append(argv[a])
save_to_json_file(new_list, arch)
