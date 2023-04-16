#!/usr/bin/python3
"""Add attribute to a class if possible"""


def add_attribute(obj, attrs, value):
    """Add an attribute to an object if possible else raise Exception
       args:
           obj: object to add attribute to
           attrs: the attribute to add
           value: value to set the attibute to
       Raises:
           TypeError: if cannot attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attrs, value)
