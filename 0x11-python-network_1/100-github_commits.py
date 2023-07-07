#!/usr/bin/python3
"""
    Authenticated into github Api using basic authentication 
    and retrieve user id.
    USAGE: ./10-my_github.py <username> <password>
"""
import requests
from sys import argv


if __name__ == "__main__":
    repo, username = argv[1:]
    url = "https://api.github.com/search/commits"
    url += f'?q=repo:{username}/{repo}&per_page=10&sort=committer-date'
    r = requests.get(url)
    try:
        for item in r.json().get("items"):
            print(f"{item['sha']} {item['commit']['author']['name']}")
    except Exception as e:
        print(e)
        pass
