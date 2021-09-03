MAXM = 100
MAXN = 100
dp = [[-1] * (MAXN + 1) for i in range(MAXM + 1)]


def LCS(s1, s2, m, n):
    if m == 0 or n == 0:
        dp[m][n] = 0
        return dp[m][n]
    if dp[m][n] != -1:
        return dp[m][n]
    if s1[m - 1] == s2[n - 1]:
        dp[m][n] = 1 + LCS(s1, s2, m-1, n-1)
        return dp[m][n]
    else:
        dp[m][n] = max(LCS(s1, s2, m-1, n), LCS(s1, s2, m, n-1))
        return dp[m][n]


if __name__ == '__main__':
    s1 = "ATCJDZEFGY"
    s2 = "BADCJEFGYT"
    print("length of LCS is: {}".format(LCS(s1, s2, len(s1), len(s2))))