#!/usr/bin/python3
#calebbaraka79@gmail.com

def search_replace(my_list, search, replace):
    """Replace all occurrencies of an element by another in a new list."""
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return (new_list)
