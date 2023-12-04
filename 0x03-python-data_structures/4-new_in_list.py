#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    invalid = idx < 0 or idx >= len(my_list)
    new_list = my_list[:]
    if invalid:
        return new_list
    new_list[idx] = element
    return new_list
