#!/usr/bin/python3
def print_args():
    import sys
    argv = sys.argv
    argv_len = len(argv) - 1
    print(argv_len, end=" ")
    print("argument" if argv_len == 1 else "arguments", end=".\n"
          if argv_len == 0 else ":\n")
    if argv_len != 0:
        for i in range(1, argv_len + 1):
            print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    print_args()
