#!/usr/bin/python3
"""
Script that takes a URL and an email,displays the response body.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email as a parameter
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    try:
        with urllib.request.urlopen(url, data) as response:

            content = response.read()
            print(content.decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error:", e.reason)
        sys.exit(1)
