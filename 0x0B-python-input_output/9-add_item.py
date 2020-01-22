#!/usr/bin/python3
from sys import argv
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


def list_append():
    """adds input args to the file"""
    try:
        app_l = load_from_json_file('./add_item.json')
    except:
        app_l = []
    for i in range(1, len(argv)):
            app_l.append(argv[i])
    save_to_json_file(app_l, './add_item.json')


if __name__ == '__main__':
    list_append()
