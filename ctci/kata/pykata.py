#!/usr/bin/env python3

print('Write a list comprehension that generates a 5 x 5 matrix with elements increasing horizontally from 1 to 25. Example:')

length = 5
x = [[length * (r - 1) + c for c in range(1, length + 1)] for r in range(1, length + 1)]

print(x)

