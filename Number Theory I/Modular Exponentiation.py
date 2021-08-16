def modularExponentiation(a, b, m):
    result = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        b //= 2
        a = (a*a)%m
    return result

if __name__ == '__main__':
    a = 50
    b = 100
    m = 13
    result = modularExponentiation(a, b, m)
    print('Modular Exponentiation: ', a, ' ^ ', b, ' (mod ', m, ') = ', result, sep= '')
