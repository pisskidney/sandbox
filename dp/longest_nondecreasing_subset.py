#!/usr/bin/python


'''
Given a sequence of N numbers - A[1] , A[2] , ..., A[N] . Find the length of
the longest non-decreasing sequence.
'''


A = (5, 3, 4, 2, 6, 7)


def max_subs(A):
    S = [1] * 1000
    for i in range(1, len(A)):
        for j in range(i):
            if S[j] + 1 > S[i] and A[j] <= A[i]:
                S[i] = S[j] + 1
    return max(S)


def main():
    print max_subs(A)


if __name__ == "__main__":
    main()
