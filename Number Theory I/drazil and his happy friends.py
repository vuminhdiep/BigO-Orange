# from math import gcd
#
# n, m = [int(i) for i in input().split()]
# x = [int(i) for i in input().split()]
# y = [int(i) for i in input().split()]
# nod = gcd(n, m)
# z = [0] * nod
# for i in range(1, x[0] + 1):
#     z[x[i] % nod] = 1
# for i in range(1, y[0] + 1):
#     z[y[i] % nod] = 1
# if sum(z) == nod:
#     print("YES")
# else:
#     print("NO")


total_m, total_fm = map(int, input().split())
h_m = list(map(int, input().split()))
h_fm = list(map(int, input().split()))

res_m = [False] * total_m
res_fm = [False] * total_fm
if h_m[0] > 0:
    for i in range(1, len(h_m)):
        res_m[h_m[i]] = True

if h_fm[0] > 0:
    for j in range(1, len(h_fm)):
        res_fm[h_fm[j]] = True

i_max = 10000
for i in range(i_max):
    invite_m = i % total_m
    invite_fm = i % total_fm

    if res_m[invite_m]:
        res_fm[invite_fm] = True

    if res_fm[invite_fm]:
        res_m[invite_m] = True

for male in res_m:
    if male is False:
        print("No")
        exit(0)

for fm in res_fm:
    if fm is False:
        print("No")
        exit(0)

print("Yes")