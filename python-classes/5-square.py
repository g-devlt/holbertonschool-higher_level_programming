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

    def my_print(self):
        if self.size == 0:
            print()
            return
        for y in range(self.size):
            for x in range(self.size):
                print('#', end="")
            print()


if __name__ == "__main__":
    Square(4).my_print()
    Square(0).my_print()
