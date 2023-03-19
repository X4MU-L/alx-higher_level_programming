#!/usr/bin/python3
for i in range(0, 10):
    for k in range(1 + i, 10):
        print("{}{}".format(i,k), end=", " if i != 8 else "\n")
