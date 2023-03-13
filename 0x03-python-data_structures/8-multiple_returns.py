#!/usr/bin/python3

def multiple_returns(sentence):
    """
    returns a tuple with the length of a string and its first character

    If the sentence is empty, the first character should be equal to None"""
    l = len(sentence)
    if sentence:
        first = sentence[0]
        return l, first
    return l, None
