#!/usr/bin/python3
"""
This module contains the class BaseGeometry.
"""


class BaseGeometry:
    """
    A class with public instance methods area and integer_validator.
    """

    def area(self):
        """
        Raises an Exception with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value:
        - if value is not an integer: raise a TypeError exception
        - if value is less or equal to 0: raise a ValueError exception
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
