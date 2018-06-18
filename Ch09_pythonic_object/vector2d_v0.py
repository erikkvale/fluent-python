"""
Starting definition of Vector2d class i.e. v0

-Included object representations:
    __str__,
    __repr__,
    __bytes__
- Included special methods
    __iter__,
    __eq__,
    __abs__,
    __bool__
"""
from array import array
import math


class Vector2d:

    TYPE_CODE = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __str__(self):
        return str(tuple(self))

    def __repr__(self):
        return "{}({},{})".format(
            type(self).__name__,
            *self
        )

    def __bytes__(self):
        return (
            bytes([ord(self.TYPE_CODE)]) +
            bytes(array(self.TYPE_CODE, self))
        )

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

