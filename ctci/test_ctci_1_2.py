from ctci_1_2_is_permutation import *

s1 = 'abcd'
s2 = 'bacd'
s3 = 'bcde'

def test_is_permutation_yes():
    assert is_permutation(s1, s2)

def test_is_permutation_no():
    assert not is_permutation(s2, s3)
