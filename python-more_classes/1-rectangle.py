#!/usr/bin/python3
"""A simple module for a basic Rectangle class
"""


class Rectangle:
    """A basic Rectangle class
    """
    def __gwidth(self):
        return self.__width

    def __swidth(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__width = value

    def __gheight(self):
        return self.__height

    def __sheight(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__height = value

    width = property(
        fget=__gwidth,
        fset=__swidth,
        doc="The width of the Rectangle"
    )

    height = property(
        fget=__gheight,
        fset=__sheight,
        doc="The height of the Rectangle"
    )

    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0

        self.width = width
        self.height = height


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
