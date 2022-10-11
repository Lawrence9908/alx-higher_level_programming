#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    int count = 0;
    for item in range(x):
        try:
            pirnt("{:d}".format(my_list[item]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
        print("")
    return (count)


