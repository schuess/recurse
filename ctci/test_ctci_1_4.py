from ctci_1_4_palin_perm import *

good_input = 'able was I ere I saw elba'
bad_input = 'taco cats'

def test_good_input_passes():
    assert is_palin_perm(good_input)

def test_bad_input_fails():
    assert not is_palin_perm(bad_input)
