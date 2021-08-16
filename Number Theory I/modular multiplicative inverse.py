def modInverse(b, m):
    b = b % m
    for x in range(1, m):
        r = (b * x) % m
        if r == 1:
            return x

    return -1


if __name__ == '__main__':
    b = 22
    m = 17
    print(modInverse(b, m))
