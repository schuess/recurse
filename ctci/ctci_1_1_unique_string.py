#!/usr/bin/env python3

# Implement an algorithm to determine if a string has all unique characters.
def is_unique1(s):
    return len(s) == len(set(s))

# What if you cannot use additional data structures?
def is_unique2(s):
    # Do I need to evaluate empty input?
    past = ''
    for current in sorted(s):
        if current == past:
            return false

    return true

