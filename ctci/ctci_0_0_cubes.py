#!/usr/bin/env python3

# print all positive integer solutions to the equation: a**3 + b**3 = c**3 + d**3
# where a-d are integers between 1 and 1000

import itertools

n = 1000 + 1
d = {}

for a, b in itertools.product(range(n), range(n)):
    d.setdefault(a**3 + b**3, []).append((a, b))

for k in d:
    print(f'a, b: {k}; c, d:{d[k]}')

