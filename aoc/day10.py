#!/usr/bin/env python3

from operator import xor
from functools import reduce
from day10f import *
nums = list(range(255 + 1))
input_file = './data/day10.in'

with open(input_file) as f:
    codes = [int(num) for num in f.read().strip().split(',')]

def parse(s):
    l = [ord(c) for c in s.strip()]
    l.extend([17, 31, 73, 47, 2])
    return l

# with open(input_file) as f: codes = parse(f.read())
# codes = parse('')

print(codes)

cp = ss = 0

#for i in range(64):

def apply_lengths(codes):
    for c in codes:
        rev_sub(nums, cp, c)
    cp = (cp + c + ss) % len(nums)
    ss += 1

# def block_gen(l):
#     for i in range(0, 256, 16):
#         yield l[i:i+16]

print(nums[4] * nums[1]) # 2928

# gen = block_gen(nums)
# dense_hash = []
# for block in gen:
#     dense_hash.append(reduce(xor, block))
# h = [hex(x)[2:].zfill(2) for x in dense_hash]
# print(''.join([hex(x)[2:] for x in dense_hash]))


