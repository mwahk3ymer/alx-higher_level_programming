#!/usr/bin/python3
"""
Script that uses GitHub API to display user id using Basic Authentication.
"""

import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: {} <username> <access_token>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    access_token = sys.argv[2]

    # Set up the authentication headers using Basic Authentication
    auth = (username, access_token)

    try:
        # Send a GET request to the GitHub API to get user information
        response = requests.get("https://api.github.com/user", auth=auth)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            user_data = response.json()
            print("Your GitHub user ID is:", user_data.get('id'))
        else:
            print("Error:", response.status_code, response.text)
    except requests.RequestException as e:
        print("Error:", e)
        sys.exit(1)
