from day10 import *


def test_shorter_than_end():
    test = [0, 1, 2, 3, 4]
    assert rev_sub(test, 0, 3, debug=1) == [2, 1, 0, 3, 4]

def test_longer_than_end():
    test = [0, 1, 2, 3, 4]
    assert rev_sub(test, 4, 2, debug=1) == [4, 1, 2, 3, 0]


