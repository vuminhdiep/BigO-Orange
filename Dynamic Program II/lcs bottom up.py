MAXM = 100
MAXN = 100
dp = [[-1] * (MAXN + 1) for i in range(MAXM + 1)]


def LCS(s1, s2, m, n):
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]


if __name__ == '__main__':
    s1 = "ATCJDZEFGY"
    s2 = "BADCJEFGYT"
    print("length of LCS is: {}".format(LCS(s1, s2, len(s1), len(s2))))