#!/usr/bin/python3
"""Defines append write function."""

#!/usr/bin/python3
"""Defines append write function."""

def append_write(filename="", text=""):
    """
    Append the content of the string at the end of file
    
    Args:
        filename (str): The name of the file to write/append to.  
        text (str): The string to append to the file.

    Returns:
        Number of charachers written/appended to the file.
    """
    with open(filename, "a", encodin="utf-8") as file:
        return file.write(text)
