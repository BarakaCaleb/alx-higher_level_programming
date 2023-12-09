#!/usr/bin/python3

# Caleb Baraka


"""Defines a JSON-to-object function."""

import json

def from_json_string(my_str):
    """Return the python object reprsentation of a JSON string."""

    return json.loads(my_str)
