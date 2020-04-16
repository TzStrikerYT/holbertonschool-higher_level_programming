#!/usr/bin/python3
""" Displays de headers """
if __name__ == "__main__":
    import requests
    from sys import argv

    request = requests.get(argv[1])
    print("{}".format(request.headers.get("X-Request-Id")))
