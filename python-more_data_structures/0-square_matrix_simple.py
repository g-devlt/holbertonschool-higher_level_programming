#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[y**2 for y in x] for x in matrix]


if __name__ == "__main__":
    print(square_matrix_simple([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))
