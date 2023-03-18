#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    if isinstance(roman_string, str) and roman_string:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}
        for i in range(len(roman_string)):
            if roman_string[i] == "X" and roman_string[i - 1] == "I":
                num -= 2
            num += roman[roman_string[i]]
        return (num)
    return (num)
