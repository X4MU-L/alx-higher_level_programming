#!/usr/bin/python3
def uppercase(str_):
    for idx, c in enumerate(str_):
        if ord(c) >= 97 and ord(c) <= 122:
            print("{}".format(chr(ord(c) - 32)),
                  end="" if idx != len(str_) - 1 else "\n")
        else:
            print("{}".format(c), end="" if idx != len(str_) - 1 else "\n")
