#!/usr/bin/python3
"""
    Send a get request using requests and print X-Request-Id in the header
"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    print(f"{r.headers.get('X-Request-Id')}")
