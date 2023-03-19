#!/usr/bin/python3
def uppercase(str_):
    for c in str_:
        print("{}".format(chr(ord(c) - 32)
                          if ord(c) >= 97 and ord(c) <= 122 else c),
              end="")
    print()
