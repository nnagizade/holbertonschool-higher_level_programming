#!/usr/bin/python3
"""
Module for Abstract Animal Class task.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class Animal."""

    @abstractmethod
    def sound(self):
        """Abstract method sound."""
        pass


class Dog(Animal):
    """Subclass Dog inheriting from Animal."""

    def sound(self):
        """Returns the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Subclass Cat inheriting from Animal."""

    def sound(self):
        """Returns the sound of a cat."""
        return "Meow"
