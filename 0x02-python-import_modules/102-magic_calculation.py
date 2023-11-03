#!/usr/bin/python3
# Caleb Baraka <calebbaraka79@gmail.com>

def magic_calculation(a, b):
    """Match byte code provided by ALX."""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return(c)
    else:
        return(sub(a, b))
