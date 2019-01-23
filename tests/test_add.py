"""
Tests the add() function of the calculator.
"""
from calculator import add

def test_two_plus_two():
    #if given 2 and 2 as paramters, 4 should be returned
    assert add(2,2) == 4
