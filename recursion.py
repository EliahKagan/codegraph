#!/usr/bin/env python

"""Auxiliary code to produce input for visualizing recursion."""


def nest(seed, degree, height):
    """
    Create a nested tuple from a seed, branching degree, and height.

    The seed will be a leaf or subtree.

    >>> nest('hi', 2, 0)
    'hi'
    >>> nest('hi', 2, 1)
    ('hi', 'hi')
    >>> nest('hi', 2, 2)
    (('hi', 'hi'), ('hi', 'hi'))
    >>> nest('hi', 2, 3)
    ((('hi', 'hi'), ('hi', 'hi')), (('hi', 'hi'), ('hi', 'hi')))
    >>> from pprint import pprint
    >>> pprint(nest('hi', 3, 3))
    ((('hi', 'hi', 'hi'), ('hi', 'hi', 'hi'), ('hi', 'hi', 'hi')),
     (('hi', 'hi', 'hi'), ('hi', 'hi', 'hi'), ('hi', 'hi', 'hi')),
     (('hi', 'hi', 'hi'), ('hi', 'hi', 'hi'), ('hi', 'hi', 'hi')))
    """
    if degree < 0:
        raise ValueError('degree cannot be negative')
    if height < 0:
        raise ValueError('height cannot be negative')
    return seed if height == 0 else nest((seed,) * degree, degree, height - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
