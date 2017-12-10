#!/usr/bin/evn python3

def rev_sub(x, start, length, debug=0):
    """Reverses a substring of a list
       and returns the modified list"""
    end = start + length
    edge = len(x) - start
    left = length - edge
    if debug == 1:
        print(f'\n### start: {start}; length: {length}; edge: {edge}; left: {left}')

    if end < len(x):
        x[start:end] = x[start:end][::-1]
    else:
        r = []
        r.extend(x[start:])
        r.extend(x[:left])
        rd = list(reversed(r))
        x[start:] = rd[:edge]
        x[:left] = rd[edge:]
    return x


def apply_lengths(l, codes):
    """Use a list of codes to permute a list of digits (l)
       Most of the work is done in rev_sub"""
    for c in codes:
        rev_sub(nums, cp, c)
    cp = (cp + c + ss) % len(nums)
    ss += 1
    return nums
