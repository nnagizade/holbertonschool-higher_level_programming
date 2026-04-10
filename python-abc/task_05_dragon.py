#!/usr/bin/env python3
"""
Module defining Mixins for swimming and flying, and a Dragon class
"""


class SwimMixin:
    """Provides swimming functionality"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Provides flying functionality"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that can swim and fly via Mixins, 
    and also has its own roar ability.
    """
    def roar(self):
        print("The dragon roars!")
