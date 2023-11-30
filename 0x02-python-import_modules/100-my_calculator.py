#!/usr/bin/python3
def calculator():
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv
    argv_len = len(argv)
    if argv_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if argv[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    string = "{} {} {} = {}"
    if operator == "+":
        print(string.format(a, operator, b, add(a, b)))
    elif operator == "-":
        print(string.format(a, operator, b, sub(a, b)))
    elif operator == "*":
        print(string.format(a, operator, b, mul(a, b)))
    elif operator == "/":
        print(string.format(a, operator, b, div(a, b)))


if __name__ == "__main__":
    calculator()
