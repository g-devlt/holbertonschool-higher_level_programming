#!/usr/bin/python3
"""A module that holds class comparisons functions
"""

def is_kind_of_class(obj, a_class : type):
    """Returns True if the object is an instance of a class or a subclass of a_class"""
    return isinstance(obj, a_class)
