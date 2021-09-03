def LCSrecursion(s1, s2, m, n):
    if m == 0 or n == 0:
        return 0
    if s1[m-1] == s2[n-1]:
        return 1 + LCSrecursion(s1, s2, m-1, n-1)
    else:
        return max(LCSrecursion(s1, s2, m, n-1), LCSrecursion(s1, s2, m-1, n))


if __name__ == '__main__':
    s1 = "ED"
    s2 = "ECDG"
    print("Length of LCS is {}".format(LCSrecursion(s1, s2, len(s1), len(s2))))