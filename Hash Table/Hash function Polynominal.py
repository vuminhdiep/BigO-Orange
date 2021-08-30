def polyHash(keys):
    hashValue = 0
    a = 33
    for i in range(len(keys)):
        hashValue = ord(keys[i]) + a * hashValue
    return hashValue & 0x7FFFFFF


if __name__ == '__main__':
    keys = 'Anne'
    print(polyHash(keys))