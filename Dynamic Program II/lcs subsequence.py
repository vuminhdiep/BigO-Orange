MAXM = 100
MAXN = 100
MAXP = 100


def LCS(s1, s2, s3, m, n, p):
    dp = [[[-1] * (MAXP + 1) for j in range(MAXN + 1)]
         for k in range(MAXM + 1)]

    ''' Following steps build dp[m+1][n+1][o+1] in
    bottom up fashion. Note that dp[i][j][k]
    contains length of LCS of X[0..i-1] and
    Y[0..j-1] and Z[0.....k-1] '''
    for i in range(m + 1):
        for j in range(n + 1):
            for k in range(p + 1):
                if i == 0 or j == 0 or k == 0:
                    dp[i][j][k] = 0

                elif s1[i - 1] == s2[j - 1] and s1[i - 1] == s3[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1

                else:
                    dp[i][j][k] = max(max(dp[i - 1][j][k], dp[i][j - 1][k]), dp[i][j][k - 1])

    # dp[m][n][o] contains length of LCS for
    # X[0..n-1] and Y[0..m-1] and Z[0..o-1]
    return dp[m][n][p]


# Driver program to test above function

if __name__ == '__main__':
    T = int(input())
    while T > 0:
        m, n, p = map(int, input().split())
        s1, s2, s3 = map(str, input().split())
        print(LCS(s1, s2, s3, m, n, p))
        T -= 1

