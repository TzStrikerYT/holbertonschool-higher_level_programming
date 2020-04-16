#!/usr/bin/python3
""" Displays de headers """
if __name__ == "__main__":
    import requests
    from sys import argv

    with urllib.request.urlopen(argv[1]) as response:
        header = response.info()

    print("{}". format(header.get("X-request-Id")))
