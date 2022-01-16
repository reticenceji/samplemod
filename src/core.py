"""
My awesome library
"""

# -*- coding: utf-8 -*-
def add(a:int,b:int) -> int:
    """[summary]

    Args:
        a (int): [description]
        b (int): [description]

    Returns:
        int: [description]

    >>> add(1,1)
    2
    """
    return a+b

def test_add():
    assert add(1,2)==3

