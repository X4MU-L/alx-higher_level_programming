#!/usr/bin/python3
"""
   from the command line gets the email address and send a post
   request to the server with the email address as data
"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    data = parse.urlencode({"email": argv[2]})
    data = data.encode("utf-8")
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        print(response.read())
