#!/usr/bin/python3
""" Returns dictionary description with a simple
data structure for a JSON serialization of an object
"""


def class_to_json(obj):
    """ dictionary description of an obj """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
