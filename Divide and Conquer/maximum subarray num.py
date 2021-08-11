def maxMidSum(a, left, mid, right):
    sum = 0
    left_part_sum = -10**9
    for i in range(mid, left, -1, -1):
        sum += a[i]
        if sum > left_part_sum:
            left_part_sum= sum

    sum = 0
    right_part_sum = -10**9
    for i in range(mid+1, right+1):
        sum += a[i]
        if sum > right_part_sum:
            right_part_sum = sum

    return left_part_sum + right_part_sum

def maxSubArraySum(a, left, right):
    if left == right:
        return a[left]
    mid = (left + right)//2
    max_sum_left = maxSubArraySum(a, left, mid)
    max_sum_right = maxSubArraySum(a, mid+1, right)
    max_sum_mid = maxMidSum(a, left, mid, right)

    return max(max_sum_left, max_sum_mid, max_sum_right)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print("Maximum subarray sum is: {}".format(maxSubArraySum(a, 0, n-1)))