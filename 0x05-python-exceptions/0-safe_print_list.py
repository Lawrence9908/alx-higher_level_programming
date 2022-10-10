#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for item in range(x):
            print(item, end='')
    except:
        print("Out of Index Error")
