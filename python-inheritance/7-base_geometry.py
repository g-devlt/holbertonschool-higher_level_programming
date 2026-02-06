#!/usr/bin/python3
"""A module for BaseGeometry
"""


class BaseGeometry():
    """BaseGeometry class
    A class to handle geometry
    """

    def area(self):
        """Returns or prints the area of the object
        """
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """Used to validate an integer value
        value must be > 0 and an integer
        """

        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
