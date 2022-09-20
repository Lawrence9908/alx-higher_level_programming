#!/usr/bin/python3

for number in range(0, 98):
    if number <= 9:
        print("{0} = 0x{1}".format(number, number))
    elif number == 10:
        print("{0} = 0x{1}".format(number, "a"))
    elif number == 11:
        print("{0} = 0X{1}".format(number, "b"))
    elif number == 12:
        print("{0} = 0x{1}".format(number, "c"))
    elif number == 13:
        print("{0} = 0x{}".format(number, "d"))
    elif number == 14:
        print("{0} = 0x{1}".format(number. "e"))
    elif number == 15:
        print("{0} = 0x{1}".format(number, "f"))
    elif number >= 16:
        print("{0} = 0x{}".format(number, (number - 6)))
