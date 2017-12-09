#!/usr/bin/env python3

import re

with open('./data/day9.in') as f: text_raw = f.read()

text_minus_cancels = re.sub(r'!.', '', text_raw)
text_minus_garbage, num_matches = re.subn(r'<.*?>', '', text_minus_cancels)
garbage_count = len(text_minus_cancels) - len(text_minus_garbage) - 2 * num_matches

score = level = 0

for c in text_minus_garbage:
    if c == '{':
        level += 1
    if c == '}':
        score += level
        level -= 1

print(f'score: {score}; garbage_count: {garbage_count}; num_matches: {num_matches}')


