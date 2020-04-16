#!/usr/bin/python3
""" Displays email request """

if __name__ == "__main__":
    import requests
    from sys import argv

    email = {"email": argv[2]}
    request = requests.post(argv[1], data=email)
    print(request.text)
