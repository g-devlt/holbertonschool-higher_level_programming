#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    res = set()
    for x in set_1:
        if x not in set_2:
            res.add(x)
    for x in set_2:
        if x not in set_1:
            res.add(x)
    return res
