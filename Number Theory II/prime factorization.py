def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a

def phi_upgrade(n):
    result = n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result = (result // i) * (i - 1)
        if n > 1:
            result = (result // n) * (n-1)
        return result


if __name__ == "__main__":
    n = 80798284478113
    print('phi(', n, ') =', phi_upgrade(n), sep= '')