#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    return [element if(idx == i) else x for (i, x) in enumerate(my_list)]


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    print(new_in_list(a, 1, 10))
    print(a)
