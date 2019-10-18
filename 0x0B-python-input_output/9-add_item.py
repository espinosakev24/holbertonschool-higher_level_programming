#!/usr/bin/python3
"""Script that adds elements to a list in json notation"""
from sys import argv
from os.path import isfile
arch = "add_item.json"
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
if not isfile(arch):
    save_to_json_file([], arch)
new_list = load_from_json_file(arch)
for a in range(1, len(argv)):
    new_list.append(argv[a])
save_to_json_file(new_list, arch)
