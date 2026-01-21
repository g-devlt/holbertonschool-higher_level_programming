#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for x in range(len(my_list)):
        print(my_list[-(x + 1)])


if __name__ == "__main__":
    print_reversed_list_integer([1, 2, 3, 4, 5])