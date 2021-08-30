def JSHash(keys):
    hashValue = 1315423911
    a = 5
    b = 2
    for i in range(len(keys)):
        x = hashValue << a
        y = hashValue >> b
        hashValue ^= (x + ord(keys[i]) + y) & 0xFFFFFFF
    return hashValue & 0x7FFFFFF

if __name__ == '__main__':
    keys = 'Anne'
    print(JSHash(keys))