#!/usr/bin/python3
"""
Script that takes a URL, sends a request-Id in the response heade.
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
