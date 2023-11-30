#!/usr/bin/python3
def calculator():
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{} + {} = {:d}".format(a, b, add(a, b)))
    print("{} - {} = {:d}".format(a, b, add(a, b)))
    print("{} * {} = {:d}".format(a, b, mul(a, b)))
    print("{} / {} = {:d}".format(a, b, div(a, b)))


if __name__ == "__main__":
    calculator()
