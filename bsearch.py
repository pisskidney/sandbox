#!/usr/bin/python
import math


def bs(A, i, j, v):
    if i > j:
        return None
    mid = int(math.floor((i + j) / 2))
    if (A[mid] == v):
        return mid
    elif (A[mid] < v):
        return bs(A, mid + 1, j, v)
    else:
        return bs(A, i, mid - 1, v)


def main():
    A = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    print bs(A, 0, len(A) - 1, 4)


if __name__ == "__main__":
    main()
