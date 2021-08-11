def PrintAns(a):
    for i in range(len(a)):
        print(a[i], end=' ')


def Combination(a, n, left, k):
    if k == 0:
        PrintAns(a)
        print()
        return
    for i in range(left, n + 1):
        a.append(i)
        Combination(a, n, i + 1, k - 1)
        a.pop()


if __name__ == '__main__':
    n = 6
    k = 4
    a = []
    Combination(a, n, 1, k)
