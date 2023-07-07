#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) and uses the GitHub API to display your id

Usage: ./10-my_github.py <username> <password>
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    api_url = "https://api.github.com/user"

    try:
        response = requests.get(api_url, auth=(username, password))
        response.raise_for_status()

        data = response.json()
        user_id = data["id"]
        print("User ID:", user_id)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", str(e))
        sys.exit(1)
