#!/usr/bin/python3
for digit in range(0, 10):
    for number in range(digit + 1, 10):
        if digit ==8 and number == 9:
            print("{}{}".format(digit, number))
        else:
            print("{}{}".format(digit, number), end=", ")
