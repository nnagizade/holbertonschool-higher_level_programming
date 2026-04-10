#!/usr/bin/python3
"""
Module for VerboseList class.
"""


class VerboseList(list):
    """A class that extends list and prints notifications on changes."""

    def append(self, item):
        """Adds an item and prints a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Extends the list and prints a notification with the count."""
        count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Removes an item and prints a notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pops an item and prints a notification."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
