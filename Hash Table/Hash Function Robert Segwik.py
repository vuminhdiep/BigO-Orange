def RSHash(keys):
    a = 63689
    b = 378551
    hashValue = 0
    for i in range(len(keys)):
        hashValue = hashValue * a + ord(keys[i]) & 0x7FFFFFF
        a = a * b & 0x7FFFFFF
    return hashValue & 0x7FFFFFF

if __name__ == '__main__':
    keys = 'Anne'
    print(RSHash(keys))
