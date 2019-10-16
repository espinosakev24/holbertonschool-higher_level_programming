#!/usr/bin/python3
"""Module of save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """save to json file function"""
    with open(filename, "w", encoding="utf-8") as fd:
        fd.write(json.dumps(my_obj))
