def write_file(filename="", text=""):
    """
    Function that write content to the file.
    """
    with open(filename, encoding="utf-8") as my_file:
        my_file.write(text)