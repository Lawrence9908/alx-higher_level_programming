#!/usr/bin/python3

def islower(c):
    #ord() function finds the unicode of an alphabet
    if ord(c) in range(97, 123):
        return True
    else:
        return False
