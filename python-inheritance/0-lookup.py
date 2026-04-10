#!/usr/bin/python3
"""
This module provides a function to lookup object attributes.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    """
    return dir(obj)
