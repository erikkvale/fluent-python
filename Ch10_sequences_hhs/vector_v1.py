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

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (
            bytes([ord(self.TYPE_CODE)]) +
            bytes(self._components)
        )