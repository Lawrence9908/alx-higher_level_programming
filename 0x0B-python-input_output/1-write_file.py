#!/usr/bin/python3
"""Defiens the write file function."""

def write_file(filename="", text=""):
    """
    Write contenof a string to the file.

    Args:
        filename(str): name of the file to write.
        text(str): text to write to the file.
    Returns:
        The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)