#!/usr/bin/python3
"""
A class that Contains an area method that is not implemented
"""


class BaseGeometry:
    """empty class"""
    def area(self):
        """area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator method"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
