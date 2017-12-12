from operator import xor
from functools import reduce

def r(v, p, e):
    for (i,j) in zip(range(p,e),range(e-1,p,-1)):
        if i >= j: return e
        v[i&255],v[j&255] = v[j&255],v[i&255]
    return e # why return e? e happens to be the next value of the pointer, so we can do the side efffect + calculate our next value

def round(v, n, lengths):
    reduce(lambda p, i: i + r(v, p, p+lengths[i % len(lengths)]), range(n*len(lengths)), 0) # 0 is the default value for the accumulator; i is skip; p is pointer (= accumulator)

with open('./data/day10.in') as f: input = f.readline().strip()

v = range(256)
round(v, 1, [int(i) for i in input.split(',')])
print(v[0]*v[1])

v = range(256)
round(v, 64, [ord(c) for c in input] + [17, 31, 73, 47, 23])
h = ''.join('{:02x}'.format(reduce(xor, v[i:i+16])) for i in range(0,256,16))
print(h)

