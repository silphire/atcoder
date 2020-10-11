aa = list(map(int, input().split()))
for i in range(2 ** 4):
    e = 0
    n = 0
    for j in range(4):
        if (i >> j) & 1 == 0:
            e += aa[j]
        else:
            n += aa[j]
    if e == n:
        print('Yes')
        exit(0)
print('No')