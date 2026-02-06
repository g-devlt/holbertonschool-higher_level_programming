#!/usr/bin/python3
"""A module that holds class comparisons functions
"""


def inherits_from(obj, a_class):
    """A function that checks wether an object
    is an instance of a subclass of a_class
    """
    a = isinstance(obj, a_class)
    b = (type(obj).__name__ == a_class.__name__)
    return (a and not b)


if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited class {}".format(a, object.__name__))
