def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a

def extendedEuclid(b, m):
    result = []
    x1 = 1
    y1 = 0
    x2 = 0
    y2 = 1
    x3 = 1
    y3 = 0
    while m != 0:
        q = b//m
        r = b % m
        x3 = x1 - q*x2
        y3 = y1 - q*y2
        x1 = x2
        y1 = y2
        x2 = x3
        y2 = y3
        b = m
        m = r

    result.append(b)
    result.append(x1)
    result.append(y1)
    return result



def modInverse(b, m):
    result = extendedEuclid(b, m)
    gcd = result[0]
    x = result[1]
    y = result[2]
    if gcd != 1:
        print("Inverse doesnt exist")
    else:
        print("Modular multiplicative inverse is:", (x + m) % m)


if __name__ == '__main__':
    b = 19
    m = 141
    modInverse(b, m)