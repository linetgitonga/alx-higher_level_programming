#!/usr/bin/python3
def fizzbuzz():
    for numb in range(1, 101):
        if numb % 3 == 0 and numb % 5 != 0:
            print('Fizz', end=' ')
        elif numb % 5 == 0 and numb % 3 != 0:
            print('Buzz', end=' ')
        elif numb % 3 == 0 and numb % 5 == 0:
            print('FizzBuzz', end=' ')
        else:
            print(numb, end=' ')
