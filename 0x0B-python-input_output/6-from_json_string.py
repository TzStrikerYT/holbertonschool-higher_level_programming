#!/usr/bin/python3
import json


def from_json_string(my_str):
    """ JSON decoder """
    return (json.loads(my_str))
