#!/usr/bin/python3
start = 122
for i in range(0, 26):
    if i % 2 == 0:
        new = start
    else:
        new = start - 32
    print(chr(new), end="")
    start -= 1
