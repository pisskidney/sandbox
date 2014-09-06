#!/usr/bin/python

'''
Which (minimal) coins from A needed to make S. (infinite nr of coins)
'''

import collections


A = (1, 3, 5)
S = 11
MAXX = 99999


def sums(A, S):
    mins = collections.defaultdict(list)
    for i in range(1, S + 1):
        mins[i].append(MAXX)
        mins[i].append(list())
    mins[0].append(0)
    mins[0].append([])

    for i in range(1, S + 1):
        for j in A:
            try:
                if j <= i and mins[i][0] > mins[i - j][0] + 1:
                    mins[i][0] = mins[i - j][0] + 1
                    mins[i][1] = mins[i - j][1] + [j]
            except IndexError:
                pass
    return '->'.join(str(i) for i in mins[S][1])


def main():
    print sums(A, S)


if __name__ == "__main__":
    main()
