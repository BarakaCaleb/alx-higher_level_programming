#!/usr/bin/python3
#calebbaraka79@gmail.com

def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys."""
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
