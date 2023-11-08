#!/usr/bin/python3
#calebbaraka79@gmail.com

def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all multiplied by 2."""
    return ({k: a_dictionary[k] * 2 for k in a_dictionary})
