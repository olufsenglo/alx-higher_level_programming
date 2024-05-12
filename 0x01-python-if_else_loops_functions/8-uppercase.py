#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if islower(char):
            print(format(toupper(char)), end="")
        else:
            print(char, end="")
    print()


def islower(str):
    return 97 <= ord(str) <= 122


def toupper(char):
    ascii_val = ord(char)
    upper_val = ascii_val - 32
    return chr(upper_val)


uppercase("This is Cool")
