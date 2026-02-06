#!/usr/bin/python3
"""A module that holds class comparisons functions
"""


def inherits_from(obj, a_class):
    a = isinstance(obj, a_class)
    b = not (type(obj).__name__ == a_class.__name__)
    return (a and b)
