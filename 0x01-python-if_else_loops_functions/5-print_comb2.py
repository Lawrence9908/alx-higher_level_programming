#!/usr/bin/python3

for number in range(0, 99):
    if  number < 9:
        print("0{}, ".format(number))
    elif number > 9:
        print("{0}, ".format(number))
