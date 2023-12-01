#!/usr/bin/python3
"""
Script that takes a URL and an email displays the response body.
"""

import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare data to be sent in the POST request
    data = {'email': email}

    try:

        response = requests.post(url, data=data)

        # Display the body of the response
        print(response.text)
    except requests.RequestException as e:
        print("Error:", e)
        sys.exit(1)
