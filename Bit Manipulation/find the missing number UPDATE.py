def computeXOR(n):

    #If n is a multiple of 4
    if n % 4 ==0:
        return n

    #If n%4 gives remainder 1
    if n%4 == 1:
        return 1

    #If n%4 gives remainder 2
    if n % 4 == 2:
        return n+1

    #If n % 4 gives remainder 3
    return 0

def getMissingNo(a,n):
    xor_array = a[0]
    xor = computeXOR(n+1)
    for i in range(1,n):
        xor_array = xor_array ^ a[i]
    return xor ^ xor_array