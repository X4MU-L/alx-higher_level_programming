#!/usr/bin/python3
"""
Send a post request using requests
"""
import requests
from sys import argv

if __name__ == "__main__":
    q = "" if len(argv) == 1 else argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        r = r.json()
        if len(r) != 0:
            print(f"[{r['id']}] {r['name']}")
        else:
            print("No result")
    except Exception as e:
        print("Not a valid JSON")
