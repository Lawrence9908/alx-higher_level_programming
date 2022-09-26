#!/usr/bin/python3

def no_c(my_string):
    copy_str = [stri for stri in my_string if stri != 'c' or stri != 'C']
    return ("".join(copy_str))
