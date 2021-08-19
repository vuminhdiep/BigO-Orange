k = int(input())
n = sorted(list(map(int, input())))
i = 0
sum_digits_n = sum(n)
MAXIMUM_SUM_OF_DIGITS = 9
while sum_digits_n < k:
    sum_digits_n += MAXIMUM_SUM_OF_DIGITS - n[i]
    i += 1
print(i)