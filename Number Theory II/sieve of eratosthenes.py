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

if __name__ == "__main__":
    n = 25
    primes = sieveOfEratosthenes(n)
    for i in range(len(primes)):
        print(primes[i], end=' ')
    print()