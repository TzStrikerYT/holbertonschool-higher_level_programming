#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    from sys import argv

    js = {"q": ""} if len(argv[1]) == 1 else {"q": argv[1]}

    try:
        request = requests.post("http://0.0.0.0:5000/search_user", data=js)
        json = request.json()

        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
