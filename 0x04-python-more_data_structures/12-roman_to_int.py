#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    if isinstance(roman_string, str) and roman_string:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}
        units = ["X", "V", "D", "C", "L", "M"]
        tens = ["L", "C", "M"]
        for i in range(len(roman_string)):
            if roman_string[i] in units and roman_string[i - 1] == "I":
                num -= 2
            if roman_string[i] in tens and roman_string[i - 1] == "X":
                num -= 10
            num += roman[roman_string[i]]
        return (num)
    return (num)
