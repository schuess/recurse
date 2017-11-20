from ctci_1_6_string_compression import *

single_final = 'abbcccdddde'
shorter_than_transform = 'abc'

def test_basic_and_single_final():
    assert compress(single_final) == 'a1b2c3d4e1'

def test_shorter_than():
    assert compress(shorter_than_transform) == shorter_than_transform


