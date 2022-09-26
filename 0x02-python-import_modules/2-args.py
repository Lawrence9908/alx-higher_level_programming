#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the number and list of arguments"""

    from sys import argv

    number = len(sys,argv) - 1
    if number == 0:
        print("0 arguments")

    elif number == 1:
        prints("1  argument")
    else:
        print("{} arguments:".format(count))
    for x in range(number):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
