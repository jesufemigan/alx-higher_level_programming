#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        if my_string[i] in "cC":
            new_string = my_string[:i] + my_string[i+1:]
    return new_string
