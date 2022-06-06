n = int(input())
aa = []
for i in range(n):
    a = []
    for j in range(i + 1):
        if j == 0 or j == i:
            a.append(1)
        else:
            a.append(aa[i - 1][j - 1] + aa[i - 1][j])
    aa.append(a)
    print(*a)