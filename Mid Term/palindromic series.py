t = int(input())
for i in range(t):
    s = input()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    l2 = list(s)

    n = int(s)
    char = 0
    while n > 0:
        r = n % 10
        char = char + r
        n = n // 10
    i = 0
    palindrome_str = ""
    #Write string with character according to indices in alphabet
    while i < char:
        j = 0
        while j < len(l2) and i < char:
            k = int(l2[j])
            palindrome_str = palindrome_str + alphabet[k]
            j += 1
            i += 1

    if palindrome_str == palindrome_str[::-1]:
        print("YES")
    else:
        print("NO")
