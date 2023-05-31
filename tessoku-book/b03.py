n = int(input())
aa = list(map(int, input().split()))
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if aa[i] + aa[j] + aa[k] == 1000:
                print('Yes')
                exit()
print('No')