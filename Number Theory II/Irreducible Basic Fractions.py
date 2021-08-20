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

def sieveOfEratosthenes(n):
    mark = [True] * (n + 1)
    primes = []
    mark[0] = mark[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if mark[i] == True:
            for j in range(i * i, n + 1, i):
                mark[j] = False
    for i in range(2, n+1):
        if mark[i] == True:
            primes.append(i)
    return primes

n = int(input())
count = 0
while n != 0:
    count = phi_upgrade(n)
    print(count)
    n = int(input())



