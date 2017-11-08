#!/usr/bin/env python

def inc(character):
    return chr(ord(character) + 1)

a = expand('a')
b = expand(2 * 'b')
c = expand(2 * 'c')

short_list = [a, b, c]
long_list = [short_list, 2 * short_list, 3 * short_list]

# from listpractice import *

### using list comprehensions...

# check a, b, c, short_list, long_list exist
# get length of lists in long_list
# get length of lists in short_list
# for every list in long_list, get its length
# increment every character in the lists in short_list -- flatten the lists
# increment every character in the lists in short_list -- maintain the nesting

