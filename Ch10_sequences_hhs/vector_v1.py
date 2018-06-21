"""
For
"""
from array import array
import reprlib
import math


class Vector:
    TYPE_CODE = 'd'

    def __init__(self, components):
        self._components = array(self.TYPE_CODE, components)

    def __iter__(self):
        return iter(self._components)
    