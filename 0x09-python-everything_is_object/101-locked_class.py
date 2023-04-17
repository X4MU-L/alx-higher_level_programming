#!/usr/bin/python3
"""Defines a Locked class"""


class LockedClass:
    """Users are prevented from adding attribute to the instance
       of the locked class except for the allowed attribute using
       __slots__
    """
    __slots__ = ["first_name"]
