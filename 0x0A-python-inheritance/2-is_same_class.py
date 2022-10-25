#!/usr/bin/python3
"""
return true if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Notes:
        use type() to get specific class
        use isinstance() to get class and any parent classes too
        use issubclass() to get what object is a subclass of
    Return:
        True if obj is exactly an instance of specified class
    """
    return type(obj) == a_class
