TABLE_SIZE = 11


class Node:
    def __init__(self, key=""):
        self.key = key
        self.next = None


class HashTable:
    def __init__(self):
        self.head = None
        self.count = 0


hashTable = []


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
    index = JSHash(key) % TABLE_SIZE
    newNode = Node(key)
    if hashTable[index].head == None:
        hashTable[index].head = newNode
        hashTable[index].count = 1
        return
    newNode.next = hashTable[index].head
    hashTable[index].head = newNode
    hashTable[index].count += 1


def searchKey(key):
    index = JSHash(key) % TABLE_SIZE
    myNode = hashTable[index].head
    while myNode != None:
        if myNode.key == key:
            return True
        myNode = myNode.next
    return False


def deleteKey(key):
    index = JSHash(key) % TABLE_SIZE
    myNode = hashTable[index].head
    if myNode == None:
        return False
    temp = myNode
    while myNode != None:
        if myNode.key == key:
            if myNode == hashTable[index].head:
                hashTable[index].head = myNode.next
            else:
                temp.next = myNode.next
            hashTable[index].count -= 1
            del myNode
            return True
        temp = myNode
        myNode = myNode.next
    return False

def printHashTable():
    for i in range(TABLE_SIZE):
        if hashTable[i].count == 0:
            continue
        myNode = hashTable[i].head
        if myNode == None:
            continue
        print('----------Index ', i, '---------', sep='')
        j = 0
        while myNode != None:
            j += 1
            print(i, '.', j, ' ', myNode.key, sep= '')
            myNode = myNode.next

if __name__ == '__main__':
    keys = ["John", "Usha", "Summer", "Bella", "Donna", "Alice"]
    hashTable = [HashTable() for i in range(TABLE_SIZE)]
    for i in range(len(keys)):
        insertKey(keys[i])
    printHashTable()
