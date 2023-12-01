#!/usr/bin/python3
"""
Script that takes a URL, sends a request, and displays the response body.
Prints an error message if the HTTP status code is = to 400.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
