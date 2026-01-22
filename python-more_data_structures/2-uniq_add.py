#!/usr/bin/python3
def uniq_add(my_list=[]):
    a_set = set(my_list)
    res = 0
    for x in a_set:
        res += x
    return res
