#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return dict([(x, y * 2) for (x, y) in a_dictionary.items()])


if __name__ == "__main__":
    a = {"a": 2, "b": 10, "c": 15}
    print(a)
    print(multiply_by_2(a))