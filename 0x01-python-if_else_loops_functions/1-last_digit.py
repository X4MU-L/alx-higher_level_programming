#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = number
if number >= 0:
    if number % 10 > 5:
        print(f"Last digit of {number:d} is {number % 10:d}", end=" ")
        print(f"and is greater than 5")

    elif number % 10 == 0:
        print(f"Last digit of {number:d} is {number % 10:d}", end=" ")
        print(f"and is 0")

    else:
        print(f"Last digit of {number:d} is {number % 10:d}", end=" ")
        print(f"and is less than 6 and not 0")

elif number % 10 == 0:
    print(f"Last digit of {number:d} is {number % 10:d}", end=" ")
    print(f"and is 0")
else:
    print(f"Last digit of {number:d} is -{(number * -1) % 10:d}", end=" ")
    print(f"and is less than 6 and not 0")
