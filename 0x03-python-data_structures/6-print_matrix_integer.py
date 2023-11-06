#!/usr/bin/python3
#calebbaraka79@gmail.com


def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if j != (len(natrix[i]) - 1):
                print(" ", end="")
        print("")
