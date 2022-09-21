#!/usr/bin/python3

import random

number = random.rand.int(-1000, 1000)

last_digit = number % 10

if last_digit > 5:
    print("Last digit of {0} is {1} and is \
            grater than 5".format(number, last_digit))
elif last_digit == 0:
    print("Last digit of {0} is {1}".format(number, last_digit))
elif last_digit < 6 and last_digit not 0:
    print("Last digit of {0} is {1} and is less \
            than 6 and not 0".format(number, last_digit))
