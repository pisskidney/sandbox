#!/usr/bin/python


'''
Starting in the top left corner of a 2x grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.
'''

def go(n):
    dp = [[1 for i in range(n + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(n + 1):
            if i - 1 >= 0 and j - 1 >= 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n][n]


def main():
    print go(2)


if __name__ == "__main__":
    main()
