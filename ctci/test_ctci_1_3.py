from ctci_1_3_urlify import *

string_with_spaces = 'This is a string with spaces.'
urlified_string = '%20'.join(string_with_spaces.split())

def test_built_in():
    assert urlify1(string_with_spaces) == urlified_string

def test_regex():
    assert urlify2(string_with_spaces) == urlified_string

def test_in_place():
    assert urlify3(string_with_spaces) == urlified_string
