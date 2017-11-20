from ctci_1_5_one_away import *

s1 = 'late'
s2 = 'later'
s3 = 'fate'
s4 = 'lately'

def test_set_method_with_extra_letter():
    assert one_away(s1, s2)

def test_set_method_with_changed_letter():
    assert one_away(s1, s3)

def test_zero_edits_succeeds():
    assert one_away(s1, s1)

def test_two_away_fails():
    assert not one_away(s1, s4)
