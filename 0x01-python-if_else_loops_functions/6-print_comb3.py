#!/usr/bin/python3
for dgit1 in range(0, 10):
    for dgit2 in range(dgit1 + 1, 10):
        if dgit1 == 8 and dgit2 == 9:
            print("{}{}".format(dgit1, dgit2))
        else:
            print("{}{}".format(dgit1, dgit2), end=", ")
