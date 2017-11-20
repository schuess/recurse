#!/usr/bin/env python3

# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the 'true' length of the string.

# 1. built-in
def urlify1(s):
    return s.replace(' ', '%20')

# 2. regex
import re
def urlify2(s):
   return re.sub(' ', '%20', s)

# 3. in-place array modification
def urlify3(s):
    # collect indices of spaces
    space_indices = [i for i, char in enumerate(s) if char == ' ']

    # replace them from the back so indices don't change
    for i in reversed(space_indices):
        s = s[:i] + '%20' + s[i + 1:]

    return s
