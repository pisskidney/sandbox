#!/usr/bin/python
'''
A sequence of numbers is called a zig-zag sequence if the differences between
successive numbers strictly alternate between positive and negative. The first
difference (if one exists) may be either positive or negative. A sequence with
fewer than two elements is trivially a zig-zag sequence.

For example, 1,7,4,9,2,5 is a zig-zag sequence because the differences
(6,-3,5,-7,3) are alternately positive and negative. In contrast, 1,4,7,2,5 and
1,7,4,5,5 are not zig-zag sequences, the first because its first two
differences are positive and the second because its last difference is zero.

Given a sequence of integers, sequence, return the length of the longest
subsequence of sequence that is a zig-zag sequence. A subsequence is obtained
by deleting some number of elements (possibly zero) from the original sequence,
leaving the remaining elements in their original order.
'''

A = (1, 2, 3, 4, 5, 6, 7, 8, 9)
B = (70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32)
C = (1, 17, 5, 10, 13, 15, 10, 5, 16, 8)


class ZigZag(object):
    def longestZigZag(self, A):
        dp = [[1, _] for _ in range(len(A))]
        dp[0][0] = 1
        for i in range(1, len(A)):
            for j in range(0, i):
                if (dp[i][0] < dp[j][0] + 1 and
                    ((A[j] - A[i] > 0) != dp[j][1] or j == 0) and
                    A[i] != A[j]
                ):
                    dp[i][0] = dp[j][0] + 1
                    dp[i][1] = A[j] - A[i] > 0
        return max([x[0] for x in dp])


def main():
    zz = ZigZag()
    print zz.longestZigZag(A), 2
    print zz.longestZigZag(B), 8
    print zz.longestZigZag(C), 7


if __name__ == "__main__":
    main()
