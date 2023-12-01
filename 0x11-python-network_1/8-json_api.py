#!/usr/bin/python3
"""
Script that takes a letter, sends a POST request, and displays the response.
"""

import requests
import sys

if __name__ == "__main__":
    # Set the default letter to an empty string if no argument is given
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Prepare data to be sent in the POST request
    data = {'q': q}

    try:

        response = requests.post("http://0.0.0.0:5000/search_user", data=data)

        # Try to parse the response as JSON
        try:
            json_response = response.json()
        except ValueError:
            print("Not a valid JSON")
            sys.exit(1)

        # Check if the JSON is not empty and properly formatted
        if json_response:
            print("[{}] {}".format(
                json_response.get('id'),
                json_response.get('name')
                ))
        else:
            print("No result")
    except requests.RequestException as e:
        print("Error:", e)
        sys.exit(1)
