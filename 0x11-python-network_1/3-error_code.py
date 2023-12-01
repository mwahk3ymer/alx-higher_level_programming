#!/usr/bin/python3
"""
Script that takes a URL displays the response body.
Handles HTTPError exceptions and prints the HTTP status code.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    # Check if a URL is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            # Retrieve the response (decoded in utf-8)
            content = response.read()
            print(content.decode('utf-8'))
    except urllib.error.HTTPError as e:
        # Handle HTTPError and print the HTTP status code
        print("Error code:", e.code)
        sys.exit(1)
