#!/usr/bin/python3
"""A simple module for a basic Square class
"""


class Square:
    """A basic Square class
    """

    def gsize(self):
        return self.__size

    def ssize(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    size = property(
        fget=gsize,
        fset=ssize,
        doc="The length of one side of the Square"
    )

    def __init__(self, size=0):
        """Initialization for Square instances.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns the area of the Square object
        """
        return self.__size ** 2


if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
