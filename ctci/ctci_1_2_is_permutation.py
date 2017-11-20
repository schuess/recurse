#!/usr/bin/env python3

# Given two strings, write a method to decide if one is a permutation of the other

def is_permutation(s1, s2):
    return set(s1) == set(s2)

