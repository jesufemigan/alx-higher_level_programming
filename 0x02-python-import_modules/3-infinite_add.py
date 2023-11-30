#!/usr/bin/python3
def print_infinite():
    import sys
    argv = sys.argv
    sum = 0
    for i in range(1, len(argv)):
        sum += int(argv[i])
    print(sum)


if __name__ == "__main__":
    print_infinite()
