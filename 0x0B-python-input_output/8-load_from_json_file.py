#!/usr/bin/python3
"""Module of load from json"""
import json


def load_from_json_file(filename):
    """load from json file function"""
    text = ""
    with open(filename, "r", encoding="utf-8") as fd:
        text = fd.read()
        return json.loads(text)
