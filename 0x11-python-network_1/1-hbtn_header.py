#!/usr/bin/python3
"""
Script that takes a URL, sends a request, and displays X-Request-Id value in the response header.
"""

import urllib.request
import sys

if __name__ == "__main__":
    # Check if a URL is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            # Retrieve and display the value of X-Request-Id from the response header
            x_request_id = response.getheader('X-Request-Id')
            print(x_request_id)
    except urllib.error.URLError as e:
        print("Error:", e.reason)
        sys.exit(1)
