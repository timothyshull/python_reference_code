"""
A class equivalent to the class statement below would be generated by this code:

    >>> import collections
    >>> Point = collections.plainclass('Point', 'x y')
"""


class Point(object):
    __slots__ = ['x', 'y']  # save memory in the likely event there are many instances

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r}, {!r})'.format(self.x, self.y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __iter__(self, other):  # support unpacking
        yield self.x
        yield self.y
