#!/usr/bin/python3
def uppercase(str):
    """Print in uppercase."""
    for ch in str:
        if ord(ch) >= 97 and ord(c) <= 123:
            ch = chr(ord(ch) - 32)
        print("{}".format(ch), end="")
    print("")
