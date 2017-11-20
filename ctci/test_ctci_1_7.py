from ctci_1_7_rotate_matrix import *

import numpy as np

input = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
output = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

def test_numpy():
    assert np.array_equal(rotate_matrix1(input), np.array(output))

def test_list_comprehension():
    assert rotate_matrix2(input) == output

def test_map():
    assert rotate_matrix3(input) == output

def test_iteration():
    assert rotate_matrix4(input) == output


