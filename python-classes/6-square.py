#!/usr/bin/python3
"""A simple module for a basic Square class
"""


class Square:
    """A basic Square class
    """

    def gpos(self):
        return self.__position

    def spos(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(value[0], int) and value[0] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(value[1], int) and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    position = property(
        fget=gpos,
        fset=spos,
        doc="The position of the Square"
    )

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

    def __init__(self, size=0, position=(0, 0)):
        """Initialization for Square instances.
        """

        self.__size = 0
        self.size = size
        self.__position = (0, 0)
        self.position = position

    def area(self):
        """Returns the area of the Square object
        """
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
            return
        for y in range(self.position[1]):
            print()
        for y in range(self.size):
            for x in range(self.position[0]):
                print(' ', end="")
            for x in range(self.size):
                print('#', end="")
            print()


if __name__ == "__main__":
    Square(4, (2, 2)).my_print()
    Square(4, (10, 10)).my_print()
