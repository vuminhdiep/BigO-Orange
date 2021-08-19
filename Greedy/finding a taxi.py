def findingTaxi(a, k):
    result = 0
    user = []
    taxi = []
    for i in range(len(a)):
        if a[i] == 'U':
            user.append(i)

        elif a[i] == 'T':
            taxi.append(i)

    j = i = 0
    while j < len(taxi) and i < len(user):
        if abs(user[i] - taxi[j]) <= k:
            result += 1
            i += 1
            j += 1
        elif user[i] > taxi[j]:
            j += 1
        else:
            i += 1
    return result

if __name__ == '__main__':
    a = ['U', 'T', 'U', 'T', 'T', 'U', 'U', 'U', 'U', 'U', 'U','U', 'T', 'T', 'T']
    k = 3
    print("Maximum matching: ", findingTaxi(a, k))
