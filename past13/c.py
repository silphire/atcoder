n = int(input())
aa = list(map(int, input().split()))

s = set()
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            s.add(aa[i] * aa[j] * aa[k])
print(len(s))