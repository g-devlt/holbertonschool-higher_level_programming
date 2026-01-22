#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for (id, j) in enumerate(i):
            if id > 0:
                print(" ", end="")
            print("{:d}".format(j), end="")
        print("")


if __name__ == "__main__":
    print_matrix_integer([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
