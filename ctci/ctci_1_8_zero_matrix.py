#!/usr/bin/env python3

# Write an algorithm such that if an element in an M x N matrix is 0, its entire row and column are set to 0.

def zero_matrix(M):
    # len(M) is number of rows
    # len(M[0]) is number of columns
    zeros = [(r, c) for r in range(len(M)) for c in range(len(M[0])) if M[r][c] == 0]

    # use map and apply set() at the same time?
    rows, columns = zip(*zeros)

    for i in range(len(M)):
        for j in range(len(M[0])):
            if i in rows or j in rows:
                M[i][j] = 0

    return M
