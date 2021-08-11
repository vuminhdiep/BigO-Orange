def getMissingNo(a, n):
    xor = 1
    xor_array = a[0]
    for i in range(2, n+2):
        xor = xor ^ i
    for i in range(1, n):
        xor_array = xor_array ^ a[i]

    return xor ^ xor_array

if __name__ == '__main__':
    a = [1,2,3,4,6,7,8,9]
    result = getMissingNo(a, 8)
    print(result)