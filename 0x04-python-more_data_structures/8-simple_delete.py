#!/usr/bin/python3
#calebbaraka79@gmail.com

def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary."""
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
