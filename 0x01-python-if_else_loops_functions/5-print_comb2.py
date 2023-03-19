#!/usr/bin/python3
for c in range(0, 100):
    print("{:02d}".format(c), end=", " if c != 99 else "\n")
