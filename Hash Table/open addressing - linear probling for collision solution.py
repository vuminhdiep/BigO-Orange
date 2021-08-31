TABLE_SIZE = 11


class Node:
    def __init__(self, key=""):
        self.key = key
        self.marker = 0


current_size = 0
hashTable = [Node() for i in range(TABLE_SIZE)]


def JSHash(keys):
    hashValue = 1315423911
    a = 5
    b = 2
    for i in range(len(keys)):
        x = hashValue << a
        y = hashValue >> b
        hashValue ^= (x + ord(keys[i]) + y) & 0xFFFFFFF
    return hashValue & 0x7FFFFFF


def insertKey(key):

    global current_size
    index = JSHash(key) % TABLE_SIZE
    if current_size >= TABLE_SIZE:
        return False
    while hashTable[index].marker == 1:
        index = (index + 1) % TABLE_SIZE

    hashTable[index].key = key
    hashTable[index].marker = 1
    current_size += 1
    return True


def searchKey(key):
    index = JSHash(key) % TABLE_SIZE
    count = 0
    if current_size == 0:
        return -1
    while hashTable[index].marker != 0 and count <= TABLE_SIZE:
        if hashTable[index].key == key:
            if hashTable[index].marker == 1:
                return index
            return -1
        index = (index + 1) % TABLE_SIZE
        count += 1
    return -1


def deleteKey(key):
    global current_size
    index = searchKey(key)
    if index == -1:
        return False
    current_size -= 1
    hashTable[index].marker = 1
    return True


def printHashTable():
    if current_size == 0:
        return
    for i in range(TABLE_SIZE):
        if hashTable[i].marker == 1:
            print('----------Index ', i, '---------', sep='')
            print(hashTable[i].key)


if __name__ == '__main__':
    keys = ["John", "Usha", "Summer", "Bella", "Donna", "Alice"]
    for i in range(len(keys)):
        insertKey(keys[i])
    printHashTable()
