segment_tree = [0] * (10 ** 6)


def update(index):
    while index < len(segment_tree):
        segment_tree[index] += 1
        index += index & -index


def query(index):
    s = 0
    while (index > 0):
        s += segment_tree[index]
        index -= index & -index
    return s


def main(n, a):
    ans = 0
    count = {}
    left = [0] * n
    right = [0] * n

    for i in range(n):
        count[a[i]] = count.get(a[i], 0) + 1
        left[i] = count[a[i]]

    count.clear()

    for i in range(n - 1, -1, -1):
        count[a[i]] = count.get(a[i], 0) + 1
        right[i] = count[a[i]]
        if i < n - 1:
            ans += query(left[i] - 1)
        update(right[i])

    print(ans)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    main(n, a)
