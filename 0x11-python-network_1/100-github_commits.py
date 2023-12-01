#!/usr/bin/python3
"""
Script that uses GitHub API to list 10 commits of a repository by a user.
"""

import requests
import sys

if __name__ == "__main__":
    # Check command-line arguments
    if len(sys.argv) != 3:
        print("Usage: {} <repository_name> <owner_name>".format(sys.argv[0]))
        sys.exit(1)

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Set up the GitHub API URL for retrieving commits
    api_url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])

    try:
        # Send a GET request to the GitHub API to get the commits
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            commits = response.json()[:10]  # Take the first 10 commits
            for commit in commits:
                sha = commit['sha']
                author_name = commit['commit']['author']['name']
                print(f"{sha}: {author_name}")
        else:
            print("Error:", response.status_code, response.text)
    except requests.RequestException as e:
        print("Error:", e)
        sys.exit(1)
