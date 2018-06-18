"""
Starting definition of Vector2d class i.e. v0

-Included object representations:
    __str__,
    __repr__,
    __bytes__
- Included dunder special methods
    __iter__,
    __eq__,
    __abs__,
    __bool__,
    __format__,
    from_bytes (a @classmethod)
"""
from array import array
import math


class Vector2d:
    TYPE_CODE = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

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

    def __format__(self, format_spec=''):
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, format_spec) for c in coords)
        return outer_fmt.format(*components)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def angle(self):
        return math.atan2(self.x, self.y)

    @classmethod
    def from_bytes(cls, octets):
        type_code = chr(octets[0])
        memv = memoryview(octets[1:]).cast(type_code)
        return cls(*memv)