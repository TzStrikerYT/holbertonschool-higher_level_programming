#!/usr/bin/python3
""" Displays the error code """

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    req = urllib.request.Request(argv[1])

    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()

        print("{}".format(html.decode('utf-8')))

    except urllib.error.URLError as error:
        print("Error code: {}".format(error.code))
