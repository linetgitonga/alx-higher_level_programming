#!/usr/bin/python3
""" max integer in a list
"""

def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
     a = 1
    while a < len(list):
        if list[a] > result:
            result = list[i]
        a +=1
    return result
