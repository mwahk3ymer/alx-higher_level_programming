#!/usr/bin/python3
"""
Script that takes a URL, sends a request, and displays the response body.
Prints an error message if the HTTP status code is >= to 400.
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
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Display the body of the response
        print(response.text)

        # Check if the HTTP status code is greater than or equal to 400
        if response.status_code >= 400:
            print("Error code:", response.status_code)
    except requests.RequestException as e:
        print("Error:", e)
        sys.exit(1)
