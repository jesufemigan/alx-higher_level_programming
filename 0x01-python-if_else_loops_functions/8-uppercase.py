#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            new_name = ord(ch) - 32
        else:
            new_name = ord(ch)
        print("{}".format(chr(new_name)), end="")
    print()
