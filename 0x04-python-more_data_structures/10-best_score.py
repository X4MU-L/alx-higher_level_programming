#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_score = {"score": 0, "name": ""}
        keys = list(dict.keys(a_dictionary))
        for key in keys:
            if a_dictionary[key] > best_score["score"]:
                best_score["score"] = a_dictionary[key]
                best_score["name"] = key
        return (best_score["name"])
    return (None)
