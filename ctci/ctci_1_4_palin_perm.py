#!/usr/bin/env python3

# Is this string a permutation of a palindrome?

import re

def is_palin_perm(s):
    # remove whitespace; lowercase
    s = re.sub(r'\W', '', s).lower()

    # is there at most one unpaired letter?
    unpaired_letters = [s.count(char) % 2 for char in s]
    return sum(unpaired_letters) <= 1
