#!/usr/bin/python3
"""
Script that fetches using the requests package.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)

    # Display the body of the response with tabulation before each line
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
