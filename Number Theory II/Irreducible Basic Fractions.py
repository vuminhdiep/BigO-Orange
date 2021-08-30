def eulerPhi(n):
    i = 2
    res = n

    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            res = res * (i - 1) // i
        i += 1

    if n > 1:
        res = res * (n - 1) // n
    return res


def main():
    n = int(input())
    while n != 0:
        print(eulerPhi(n))
        n = int(input())


if __name__ == '__main__':
    main()
