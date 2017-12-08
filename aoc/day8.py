#!/usr/bin/env python3

from collections import namedtuple, defaultdict

r = defaultdict(int) # registers
inx = namedtuple('inx', 'op_reg, op, op_value, eef, test_reg, test, test_value')
r['m'] = 0
dec = '-'
inc = '+'

def parse(s):
    op_reg, op, op_value, eef, test_reg, test, test_value = inx._make(s)
    return f"{eef} r['{test_reg}'] {test} {test_value}: r['{op_reg}'] {eval(op)}= {op_value}; r['m'] = max(r['m'], r['{op_reg}'])\n"

def main():
    with open('./day8/day8.in') as f: instructions = [line.strip().split() for line in f]
    all_inx = []

    for i in instructions:
        all_inx.append(parse(i))
    exec(''.join(all_inx))

    return r.pop('m'), max(r.values())

if __name__ == "__main__":
    main()


