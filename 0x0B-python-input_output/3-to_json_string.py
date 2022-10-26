#!/usr/bin/python3
"""module that give access to python json function"""
import json

"""Defiens a String to json function."""

def to_json_string(my_list):
    """
    The function return the json representation
    of a object string

    Args:
        my_list (str): The list of strings.
    
    Returns:
        String in JSON format
    """
    return json.dumps(my_list)