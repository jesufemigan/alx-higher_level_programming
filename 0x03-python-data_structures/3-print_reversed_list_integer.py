#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    [print("{:d}".format(x)) for x in my_list[::-1]]
