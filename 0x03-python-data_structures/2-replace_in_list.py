#!/usr/bin/python3
#calebbaraka79@gmail.com

def replace_in_list(my_list, idx, element):
    """Replace an element of a list ata a specific position."""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
