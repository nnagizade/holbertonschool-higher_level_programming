#!/usr/bin/python3
"""
Module for CountedIterator class.
"""


class CountedIterator:
    """An iterator that keeps track of the number of items iterated over."""

    def __init__(self, iterable):
        """
        Initialize the iterator object and a counter.
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """Returns the current value of the counter."""
        return self.counter

    def __next__(self):
        """
        Increments the counter and fetches the next item.
        Raises StopIteration if no items are left.
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """Returns the iterator object itself."""
        return self
