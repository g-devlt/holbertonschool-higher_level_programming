#!/usr/bin/python3
"""A simple module for a sorting list."""


class MyList(list):
    """A class that inherits from list.
    """

    def print_sorted(self):
        """A function that prints a sorted version of this Object"""
        print(sorted(self))


if __name__ == "__main__":
    mylist = MyList()
    mylist.append(2)
    mylist.append(3)
    mylist.append(99)
    mylist.append(1)
    print(mylist)
    mylist.print_sorted()
    print(mylist)
