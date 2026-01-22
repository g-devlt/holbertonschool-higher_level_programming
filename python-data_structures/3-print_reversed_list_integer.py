#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for x in reversed(my_list):
        print("{:d}".format(x))


if __name__ == "__main__":
    print_reversed_list_integer([1, 2, 3, 4, 5])
