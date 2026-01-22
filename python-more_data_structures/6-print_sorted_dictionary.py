#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(key, a_dictionary.get(key)))


if __name__ == "__main__":
    print_sorted_dictionary({
        "A": 1,
        "B": 'b',
        "D": [1, 2, 3],
        "C": 3.0,
    })
