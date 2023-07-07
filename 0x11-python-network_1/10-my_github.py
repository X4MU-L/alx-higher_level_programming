#!/usr/bin/python3
"""
    Authenticated into github Api using basic authentication 
    and retrieve user id.
    USAGE: ./10-my_github.py <username> <password>
"""
import requests
from sys import argv


if __name__ == "__main__":
    username, password = argv[1:]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    try:
        print(response.json().get('id'))
    except Exception as e:
        pass
