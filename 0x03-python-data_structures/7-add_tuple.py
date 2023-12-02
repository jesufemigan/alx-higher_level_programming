#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_1 = tuple_a[0]
    b_1 = tuple_b[0]
    if len(tuple_a) == 1:
        a_2 = 0
    else:
        a_2 = tuple_a[1]
    if len(tuple_b) == 1:
        b_2 = 0
    else:
        b_2 = tuple_b[1]
    return (a_1 + b_1, a_2 + b_2)
