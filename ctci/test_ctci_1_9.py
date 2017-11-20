from ctci_1_9_string_rotation import *

original = 'waterbottle'
rotation = 'erbottlewat'
close = 'erbottlewate'
not_close = 'napolean'

# Version 1
def test_default1():
    assert is_rotation1(original, rotation)

def test_close1():
    assert not is_rotation1(original, close)

def test_not_close1():
    assert not is_rotation1(original, not_close)

# Version 2
def test_default2():
    assert is_rotation2(original, rotation)

def test_close2():
    assert not is_rotation2(original, close)

def test_not_close2():
    assert not is_rotation2(original, not_close)

