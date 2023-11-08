#!/usr/bin/python3
#calebbaraka79@gmail.com

def square_matrix_simple(matrix=[]):
    """Computes square value of all integers of a matrix."""
    
    return ([list(map(lambda x: x * x, row)) for row in matrix])
