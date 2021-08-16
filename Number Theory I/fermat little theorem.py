def modularExponentiation(a, b, m):
    result = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m
    return result


def modInverse(b, m):
    res = modularExponentiation(b, m - 2, m)
    if (res * b) % m == 1:
        return res
    return -1


if __name__ == '__main__':
    b = 22
    m = 17
    print(modInverse(b, m))
