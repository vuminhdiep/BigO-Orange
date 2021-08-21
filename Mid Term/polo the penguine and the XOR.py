t = int(input())
while t > 0:

    n = int(input())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(32):
        p = [1, 0]
        c = cnt = 0
        for j in range(n):
            c ^= s[j] & 1
            s[j] >>= 1
            cnt += p[c ^ 1]
            p[c] += 1
        ans += cnt * (2 ** i)

    print(ans)
    t -= 1
