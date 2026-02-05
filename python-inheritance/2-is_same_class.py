#!/usr/bin/python3
"""A module for is_same_class
"""


class A():
    """Testing base class"""
    pass


class B(A):
    """Testing child class"""
    pass


def is_same_class(obj, a_class):
    """Returns wether obj is of the class 'a_class'"""
    return type(obj).__name__ == a_class.__name__


if __name__ == "__main__":
    print(is_same_class(B(), A))
    print(is_same_class(1, int))
