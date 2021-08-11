def shouldSwap(s, start, end):
    for i in range(start, end):
        if s[i] == s[end]:
            return False

    return True


def distinctPermutations(s, l, r):
    if l >= r:
        print(''.join(s))
        return
    for i in range(l, r):
        check = shouldSwap(s, l, i)
        if check == True:
            s[l], s[i] = s[i], s[l]
            distinctPermutations(s, l + 1, r)
            s[l], s[i] = s[i], s[l]


if __name__ == '__main__':
    s = list("AABB")
    distinctPermutations(s, 0, len(s))
