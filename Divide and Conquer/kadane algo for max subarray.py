#Dynamic Programming

def maxSubAraaySum(a):
    maxSum = a[0]
    curSum = 0
    start = end = s = 0
    for i in range(len(a)):
        curSum += a[i]
        if maxSum < curSum:
            maxSum = curSum
            start = s
            end = i
        if curSum < 0:
            curSum = 0
            s = i+1

    print("Maximum Subarray Sum:", maxSum)
    for i in range(start, end+1):
        print(a[i], end=' ')

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    maxSubAraaySum(a)