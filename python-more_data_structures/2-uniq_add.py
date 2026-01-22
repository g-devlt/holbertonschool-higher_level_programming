#!/usr/bin/python3
def uniq_add(my_list=[]):
    l = set(my_list)
    res = 0
    for x in l:
        res += x
    return res
