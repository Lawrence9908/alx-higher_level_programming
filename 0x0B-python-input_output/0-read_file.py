#!/usr/bin/python3

def read_file(filename=""):
    """
    Python function to read the content of the file into stdout.
    """

    with open(filename, encoding="utf-8") as my_content:
        #saving the read line into read_data variable
        read_data = my_content.read()
        #printing out the read line into stdout
        print(read_data)

