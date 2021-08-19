def sieveOfEratosthenes(limit):
    mark = [True] * (limit + 1)
    primes = []
    mark[0] = mark[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if mark[i] == True:
            for j in range(i * i, limit + 1, i):
                mark[j] = False
    for i in range(2, limit + 1):
        if mark[i] == True:
            primes.append(i)
    return primes


def segmentedSieve(left, right, primes):
    if left == 1:
        left += 1
    mark = [True] * (right - left + 1)
    i = 0
    while i < len(primes) and primes[i] <= right ** 0.5:
        base = (left // primes[i]) ** primes[i]
        if base < left:
            base += primes[i]
        for j in range(base, right + 1, primes[i]):
            if j != primes[i]:
                mark[j - left] = False
        i += 1
    result = []
    for i in range(left, right + 1):
        if mark[i - left] == True:
            result.append(i)
    return result

if __name__ == "__main__":
    left = 11
    right = 34
    primes = sieveOfEratosthenes(right ** 0.5)
    result = segmentedSieve(left, right, primes)
    for p in result:
        print(p, end=' ')