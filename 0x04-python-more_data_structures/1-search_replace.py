#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda x:x = replace if x == search, my_list))
