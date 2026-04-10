#!/usr/bin/python3
"""
Module for CountedIterator class.
"""


class CountedIterator:
    """An iterator that keeps track of the number of items iterated over."""

    def __init__(self, data):
        """
        Initialize the iterator object and a counter.
        """
        self.iterator = iter(data)
        self.counter = 0

    def get_count(self):
        """Returns the current value of the counter."""
        return self.counter

    def __next__(self):
        """
        Increments the counter and fetches the next item.
        """
        item = next(self.iterator)
        self.counter += 1
        return item

    def __iter__(self):
        """Returns the iterator object itself."""
        return self
