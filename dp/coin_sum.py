#!/usr/bin/python

'''
Minimum number of coins from A needed to make S. (infinite nr of coins)
'''

A = (1, 3, 5)
S = 11
MAXX = 99999


def sums(A, S):
    mins = list()
    for i in range(1, S + 1):
        mins.append(MAXX)
    mins.insert(0, 0)

    for i in range(1, S + 1):
        for j in A:
            try:
                if j <= i and mins[i] > mins[i - j] + 1:
                    mins[i] = mins[i - j] + 1
            except IndexError:
                pass
    return mins[S]


def main():
    print sums(A, S)


if __name__ == "__main__":
    main()
