#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """ crates json object from file """
    with open(filename, mode="r", encoding="utf-8") as f:
        _dict = json.loads(f.read())
        f.close()
    return _dict
