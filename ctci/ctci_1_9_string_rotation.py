#!/usr/bin/env python3

# ctci_1_9_string rotation.py

# Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, check if s2 is a rotation of s1 using only one call to isSubstring.

# E.g., waterbottle is a rotation of erbottlewat

# Naive approach
def is_rotation1(s1, s2):
    first_letter = s2[0]
    for start in [index for index, letter in enumerate(s1) if letter == first_letter]:
        if s2 == s1[start:] + s1[:start]:
            return True

    return False

# Substring approach
def is_rotation2(s1, s2):
    if s1 and s2:
        return s2 in s1 + s1 and len(s1) == len(s2)

