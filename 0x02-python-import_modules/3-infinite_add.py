#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_len = len(sys.argv) - 1
    add_sum = 0

    for i in range(arg_len):
        add_sum += int(sys.argv[i + 1])

    print(add_sum)
