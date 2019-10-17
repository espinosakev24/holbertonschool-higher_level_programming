#!/usr/bin/python3
"""module of from_json_string"""
import json


def from_json_string(my_str):
    """function to convert from js str to py obj"""
    return json.loads(my_str)
