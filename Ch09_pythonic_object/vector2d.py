from array import array
import math

class Vector2d:
    """
    A class to emulate a Python numeric type,
    in this case a 2d vector
    """

    # The class attribute for byte conversions
    type_code = 'd'

    def __init__(self, x, y):
        # Explicit conversions to numeric types
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        """
        __iter__ makes a Vector2d iterable; this is what
         makes unpacking work (e.g, x, y = my_vector).
         We implement it simply by using a generator expression
         to yield the components one after the other.
        """
        return (i for i in (self.x, self.y))

    def __repr__(self):
        """
        __repr__ builds a string by interpolating the
        components with {!r} to get their repr; because
        Vector2d is iterable, *self feeds the x and y
        components to format.
        """
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        """
        From an iterable Vector2d, it’s easy to build
        a tuple for display as an ordered pair.
        """
        return str(tuple(self))

    def __bytes__(self):
        """
        To generate bytes, we convert the typecode to
        bytes and concatenate, bytes converted from an
        array built by iterating over the instance
        """
        return (bytes([ord(self.type_code)]) +
                bytes(array(self.type_code, self)))

    def __eq__(self, other):
        """
        To quickly compare all components, build tuples
        out of the operands. This works for operands that
        are instances of Vector2d, but has issues. See
        the following warning.
        """
        return tuple(self) == tuple(other)

    def __abs__(self):
        """
        The magnitude is the length of the hypotenuse of
        the triangle formed by the x and y components.
        """
        return math.hypot(self.x, self.y)

    def __bool__(self):
        """
        __bool__ uses abs(self) to compute the magnitude,
        then converts it to bool, so 0.0 becomes False,
        nonzero is True.
        """
        return bool(abs(self))