#!/usr/bin/python3
for asc in range(97, 123):
    if chr(asc) == 'q' or chr(asc) == 'e':
        continue
    print(chr(asc).format(asc), end='')
