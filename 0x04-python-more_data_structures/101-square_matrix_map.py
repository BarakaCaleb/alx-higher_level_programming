#!/usr/bin/python3
#calebbaraka79@gmail.com

def square_matrix_map(matrix=[]):
    """Computes the square value of all integers in a matrix."""
    return (list(map(lambda x: list(map(lambda y: y ** 2, x[:])), matrix)))
