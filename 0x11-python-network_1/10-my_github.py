#!/usr/bin/python3
""" Connnect to github API """
if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv

    user = argv[1]
    passwd = argv[2]

    request = requests.get(
        "https://api.github.com/user", auth=HTTPBasicAuth(user, passwd))
    json = request.json()
    print("{}".format(json.get("id")))
