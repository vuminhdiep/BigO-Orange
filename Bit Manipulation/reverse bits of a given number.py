def bit_reversal(n):
    s = 8
    rev = 0
    while n != 0:
        # Shift left
        rev <<= 1
        # If current bit is '1'
        if n & 1 == 1:
            rev ^= 1  # XOR 1
        # Shift right
        n >>= 1
        s -= 1

    if s > 0:
        rev <<= s
    return rev


if __name__ == '__main__':
    n = 38
    rev = bit_reversal(n)
    print(n, ' (', bin(n), ')', sep='')
    print(rev, ' (', bin(rev), ')', sep='')
