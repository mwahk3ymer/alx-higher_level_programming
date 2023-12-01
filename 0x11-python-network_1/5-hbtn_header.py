#!/usr/bin/python3
"""
Script that takes a URL, sends a request, and displays the value of X-Request-Id in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if a URL is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)

        # Check if 'X-Request-Id' is present in the response headers
        if 'X-Request-Id' in response.headers:
            x_request_id = response.headers['X-Request-Id']
            print(x_request_id)
        else:
            print("X-Request-Id not found in the response headers.")
    except requests.RequestException as e:
        print("Error:", e)
        sys.exit(1)
