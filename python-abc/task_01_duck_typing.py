#!/usr/bin/python3
"""
Module for Shapes, Interfaces, and Duck Typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class Shape."""

    @abstractmethod
    def area(self):
        """Abstract method for area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for perimeter."""
        pass


class Circle(Shape):
    """Concrete class Circle."""

    def __init__(self, radius):
        """Initialize with radius."""
        self.radius = radius

    def area(self):
        """Calculate area of circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate perimeter of circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete class Rectangle."""

    def __init__(self, width, height):
        """Initialize with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area of rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter of rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter using duck typing."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
