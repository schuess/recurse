from ctci_1_1_unique_string import *

good_input = 'abcdefghij'
bad_input = 'abcdefghia'

def test_is_unique1_good():
    assert is_unique1(good_input)

def test_is_unique1_bad():
    assert not is_unique1(bad_input)

def test_is_unique2_good():
    assert is_unique1(good_input)

def test_is_unique2_bad():
    assert not is_unique1(bad_input)


