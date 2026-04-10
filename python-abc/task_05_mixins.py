#!/usr/bin/python3
"""
Module for Mixins task.
"""


class DisplayMixin:
    """Mixin to display object details dynamically."""

    def display_details(self):
        """Displays all attributes of the instance in a specific format."""
        print("-" * 20)
        for key, value in self.__dict__.items():
            print("{}: {}".format(key, value))
        print("-" * 20)


class Book(DisplayMixin):
    """Book class that uses DisplayMixin."""

    def __init__(self, title, author, pages):
        """Initialize book attributes."""
        self.title = title
        self.author = author
        self.pages = pages


class StudentList(DisplayMixin):
    """StudentList class that uses DisplayMixin."""

    def __init__(self, students):
        """Initialize student list."""
        self.students = students
