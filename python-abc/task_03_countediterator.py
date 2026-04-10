#!/usr/bin/env python3
"""
Module for CountedIterator class
"""


class CountedIterator:
    """
    An iterator that keeps track of the number of items iterated over.
    """

    def __init__(self, iterable):
        """
        Initializes the iterator and the counter.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """
        Returns the current value of the counter.
        """
        return self.count

    def __next__(self):
        """
        Fetches the next item and increments the counter.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self
