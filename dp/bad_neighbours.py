#!/usr/bin/python


'''
The old song declares Go ahead and hate your neighbor, and the residents of
Onetinville have taken those words to heart. Every resident hates his next-door
neighbors on both sides. Nobody is willing to live farther away from the towns
well than his neighbors, so the town has been arranged in a big circle around
the well. Unfortunately, the towns well is in disrepair and needs to be
restored. You have been hired to collect donations for the Save Our Well fund.
Each of the towns residents is willing to donate a certain amount, as
specified in the int[] donations, which is listed in clockwise order around the
well. However, nobody is willing to contribute to a fund to which his neighbor
has also contributed. Next-door neighbors are always listed consecutively in
donations, except that the first and last entries in donations are also for
next-door neighbors. You must calculate and return the maximum amount of
donations that can be collected.
'''


class BadNeighbors(object):
    def maxDonations(self, d):
        n = len(d)
        dp = [[d[x], True] for x in range(len(d))]
        for i in range(2, len(d) - 1):
            for j in range(i - 1):
                if dp[i][0] < dp[j][0] + d[i]:
                    dp[i][0] = dp[j][0] + d[i]
                    dp[i][1] = dp[j][1]

        for j in range(n - 2):
            if dp[n - 1][0] < dp[j][0] + d[n - 1]:
                if dp[j][1]:
                    if dp[n - 1][0] > dp[0][0]:
                        dp[n - 1][0] = dp[j][0] + d[n - 1] - d[0]
                        dp[n - 1][1] = False
                    else:
                        dp[n - 1][1] = True
                else:
                    dp[n - 1][0] = dp[j][0] + d[n - 1]
                    dp[n - 1][1] = False
        return max([dpv[0] for dpv in dp])


d = (10, 3, 2, 5, 7, 8)


def main():
    bn = BadNeighbors()
    print bn.maxDonations(d)


if __name__ == "__main__":
    main()
