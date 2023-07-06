#!/usr/bin/python3
"""Takes in a URL, email, sends a POST request and displays body of response

Use: ./6-post_email.py <url> <email>
"""
import sys
import requests


if __name == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
