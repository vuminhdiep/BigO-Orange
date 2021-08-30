# def isPrime(x):
#     # invalid input
#     if x <= 1:
#         return False
#
#     # process all potential divisors
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#
#             # no divisor found, therfore it's a prime number
#     return True
#
#
# def main():
#     N = int(input())
#     # a list to store all the prime factors of a number
#     Factors = [1]
#     while N != 0:
#         # iterate from 2 to half of the number as there can be no factor
#         # greater than half of the number.
#         for i in range(2, N // 2 + 1):
#             # check if number is a factor
#             if N % i == 0:
#                 # check if factor is also a prime
#                 if isPrime(i):
#                     # add the number to the list
#                     Factors.append(i)
#         if len(Factors) > 2:
#             # output the maximum of the factors to obtain largest prime factor
#             print(max(Factors))
#         else:
#             print(-1)
#         N = int(input())


def maxPrimeFactors(n):
    maxPrime = -1
    count = 0

    i = 2

    while i * i <= n:
        if n % i == 0:
            count += 1
            maxPrime = i

        while n % i == 0:
            n //= i

        i += 1

    if count > 0 and n > 1:
        return n
    elif count == 1:
        return -1

    return maxPrime


def main():
    N = int(input())
    while N != 0:
        print(maxPrimeFactors(N))
        N = int(input())


if __name__ == '__main__':
    main()
