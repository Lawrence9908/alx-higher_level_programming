#!/usr/bin/python3


"""Defiens the read_file function."""


def read_file(filename=""):
    """
    Read the content of the file and print it into stdout.

    Args:
       filename(str): file to read text from.

    Returns:
        The function return nothing/void
    """
    with open(filename, encoding="utf-8") as f:
        # saving the read line into read_data variable
        read_data = f.read()
        # printing out the read line into stdout
        print(read_data, end="")
