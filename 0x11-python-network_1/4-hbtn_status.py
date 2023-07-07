#!/usr/bin/python3
"""
    Send a get request using requests and print a formatted
    response
"""
import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print(f"Body response:\n\t\
- type: {type(r.text)}\n\t\
- content: {r.text}")
