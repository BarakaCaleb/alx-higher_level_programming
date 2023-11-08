#!/usr/bin/python3
#calebbaraka79@gmail.com

def multiply_list_map(my_list=[], number=0):
    """Returns a value multiplied by a number without using any loops."""
    return (list(map(lambda x: x*number, my_list)))
