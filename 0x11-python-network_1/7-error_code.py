#!/usr/bin/python3
"""
    Send a get request, print status code if error
"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    try:
        r.raise_for_status()
        print(f"{r.text}")
    except requests.exceptions.HTTPError:
        print(f"Error code: {r.status_code}")
