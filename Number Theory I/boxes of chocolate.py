T = int(input())
for _ in range(T):
    res = 0
    friends, boxes = map(int, input().split())
    for i in range(boxes):
        K = int(input())
        value = 1
        for j in range(K):
            chocolate = int(input())
            value = (value * chocolate) % boxes

        res += value

    res %= friends
    print(res)
