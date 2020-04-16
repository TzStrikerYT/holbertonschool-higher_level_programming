#!/usr/bin/python3
""" Displays de headers """
if __name__ == "__main__":
    import requests
    import sys

    request = requests.get(sys.argv[1])
    print(request.headers["X-Request-Id"])
