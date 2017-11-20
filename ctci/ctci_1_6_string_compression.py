#!/usr/bin/env python3

# Implement a method to perform basic string compression using the counts of repeated characters; return original if shorter

def compress(s):
    last = s[0]
    count = 0
    compressed = []

    for current in s:
        if current == last:
            count += 1
        else:
            compressed.append((last, count))
            last = current
            count = 1

    compressed.append((last, count)) # add whatever didn't match EOL

    r = ''
    for t in compressed:
        r += t[0] + str(t[1])
    return r if len(r) < len(s) else s
