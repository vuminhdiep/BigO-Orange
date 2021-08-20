def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


def phi(n):
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result


if __name__ == "__main__":
    n = 60
    print('phi(', n, ') =', phi(n), sep= '')