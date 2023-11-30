#!/usr/bin/python3
def uppercase(str):
    """Print in uppercase."""
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 123:
            ch = chr(ord(ch) - 32)
        print("{}".format(ch), end="")
        elif  if ord('a') <= ord(ch) <= ord('z'):
            ch = chr(ord(ch) - (ord('a') - ord('A')))
        print("{:s}".format(ch), end='')
    print("")
