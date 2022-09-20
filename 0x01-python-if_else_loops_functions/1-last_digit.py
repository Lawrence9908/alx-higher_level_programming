#!/usr/bin/python3

import random

number = random.randint(-10,10)

for intiger_number in number:
    if intiger_number > 0:
        print("is positive")
    elif intiger_number == 0:
        print("is zero")
    elif intiger_number < 0:
        print("is negative")
