#!/usr/bin/env python3

# Given an image represented by an N x N matrix where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

# Assumption: Python ints are 32 bits, so I can use an int to represent pixel location
# Question: What is the point of this 4 byte limitation?


# numpy
def rotate_matrix1(M):
    import numpy as np
    # M = np.arange(1, 16 + 1).reshape(4, 4)
    return np.transpose(np.flip(M, 0))

# list comprehension
def rotate_matrix2(M):
    # M = [[c + (r - 1) * 4 for c in range(1, 5)] for r in range(1, 5)]
    return [list(t) for t in zip(*reversed(M))]

# map
def rotate_matrix3(M):
    return list(map(list, zip(*reversed(M))))


# iterate through indices
def rotate_matrix4(M):

    # maps 0..3 to 3..0, for example
    def rotated(x, l = 4):
        # how do I reference len(M) here?
        return range(l - 1, -1, -1)[range(l).index(x)]

    to_do = [(r, c) for r in range(len(M)) for c in range(len(M))]
    done = []

    # rotate
    for coord in to_do:
        if coord not in done:
            # Could this be a 'swap' function? Would I have to pass the matrix?
            old_r, old_c = coord
            new_r, new_c = old_c, (rotated(old_r))

            # swap
            M[new_r][new_c], M[old_r][old_c] = M[old_r][old_c], M[new_r][new_c]
            done.append((new_r, new_c))
    return M


def create_test_data():
    # Usage: M = create_test_data()
    return [[c + (r - 1) * 4 for c in range(1, 5)] for r in range(1, 5)]

def run():
    print(rotate_matrix4(create_test_data()))
