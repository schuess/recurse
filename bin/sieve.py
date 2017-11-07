#!/usr/bin/env python

# accept an input, sanitize it, add a default
up_to = int(input('How far? -> ') or 17)


def primes(up_to):
    is_prime = list(range(up_to + 1))
    for p in range(2, int(up_to ** 0.5 + 1)): 
        if is_prime[p]:
            for multiple in range(p ** 2, up_to, 2 * p): 
                is_prime[multiple] = False

    return [x for x in is_prime[2: ] if x]

print(primes(up_to))





# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101
# set up a test
# explain how __main__ works
# call test from command line
# add logging

