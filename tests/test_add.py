"""
Tests the add() function of the calculator.
"""

import pytest

from calculator import add

def test_two_plus_two():
    #if given 2 and 2 as paramters, 4 should be returned
    assert add(2,2) == 4

def test_three_plus_three():
    #if given 3 and 3 as parameters, 6 should be returned
    assert add(3,3) == 6

def test_no_parameters():
    """
    If no parameters provided, return 0.
    """
    assert add() == 0

def test_one_two_three():
    #Given 1,2,3 as parameters, 6 should return
    assert add(1,2,3) == 6

def test_negative_values():
    # assert that negative values work
    assert add(-1,-1,-4)

def test_decimal_values():
    #assert that 0.1, 0.1, and 0.1 equals 0.3
    assert add(0.1, 0.1, 0.1) == pytest.approx(0.3)
