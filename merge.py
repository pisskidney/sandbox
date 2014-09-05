#!/usr/bin/python


def merge(A, p, q, r):
    res = []
    i = p
    j = q + 1
    while i <= q and j <= r:
        if A[i] < A[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(A[j])
            j += 1
    for i in range(i, q + 1):
        res.append(A[i])
    for i in range(j, r + 1):
        res.append(A[i])

    return res


def main():
    print merge([1, 3, 5, 7, 2, 4, 6, 8], 0, 3, 7)


if __name__ == "__main__":
    main()
