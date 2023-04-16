#!/usr/bin/python3
"""
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


import json


def print_logs(logs):
    """Print accumulated metrics.
    Args:
        logs (dict): The accumulated count of status codes and size.
    """
    print("File size: {}".format(logs["size"]))
    for key in sorted(logs):
        if key != "size":
            print("{}: {}".format(key, logs[key]))


def save_to_json_file(my_obj, filename):
    """pasrse a Json serializable to a string and write to a file
       Args:
           my_obj: json object to parse
    """
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """load a json object string from a file
       Args:
           filename: the file with the json object string
    """
    with open(filename, encoding="UTF-8") as f:
        return (json.load(f))


if __name__ == "__main__":
    import sys

    log_count = 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]

    try:
        logs = load_from_json_file("logs.json")
    except FileNotFoundError:
        logs = {}
    try:
        for line in sys.stdin:
            if log_count == 10:
                print_logs(logs)
                log_count = 1
            else:
                log_count += 1

            line = line.split()
            try:
                if logs.get("size", -1) == -1:
                    logs["size"] = 0
                    logs["size"] += int(line[-2])
                else:
                    logs["size"] += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in codes:
                    if logs.get(line[-2], -1) == -1:
                        logs[line[-2]] = 1
                    else:
                        logs[line[-2]] += 1
            except IndexError:
                pass

        print_logs(logs)
    save_to_json_file(logs, "logs.json")
    except KeyboardInterrupt:
        save_to_json_file(logs, "logs.json")
        print_logs(logs)
        raise
