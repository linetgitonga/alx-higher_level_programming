#!/usr/bin/python3

def no_c(my_string):
    updated_st = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            updated_st += i
    return (updated_st)
