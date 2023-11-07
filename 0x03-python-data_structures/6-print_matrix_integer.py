#!/usr/bin/python3
#calebbaraka79@gmail.com


def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    if not matrix:
        return

    for row in matrix:
        for i, num in enumerate(row):
            print("{:d}".format(num), end="")
            if i < len(row) - 1:
                print(" ", end="")
        print()
