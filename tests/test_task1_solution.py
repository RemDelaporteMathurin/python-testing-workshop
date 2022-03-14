from calculator import *


def test_add():
    assert add(1, 2) == 3
    assert add([1, 2], [2, 3]) == [3, 5]


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(2, [1, 2, 3]) == [2, 4, 6]
    assert multiply([1, 2, 3], 2) == [2, 4, 6]
    assert multiply([1, 2, 3], [2, 3, 4]) == 2*1 + 2*3 + 3*4


def test_divide():
    assert divide(2, 3) == 2/3
