from ctci_1_8_zero_matrix import *

def create_mxn_list_of_lists(m, n):
    M = [[m * r + c for c in range(m)] for r in range(n)]
    return M

def create_test_data():
    M = create_mxn_list_of_lists(3, 4)
    M[2][1] = 0
    M[3][2] = 0
    return M

# create_test_data() = [[0, 1, 2], [3, 4, 5], [6, 0, 8], [9, 10, 0]]
output = [[0, 0, 0], [0, 4, 0], [0, 0, 0], [0, 0, 0]]

def test_zero_matrix():
    assert zero_matrix(create_test_data()) == output
