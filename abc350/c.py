n = int(input())
aa = list(map(int, input().split()))

pp = {}
for i, a in enumerate(aa):
    pp[a] = i

ans = []
for i in range(n):
    a = aa[i]
    if a == i + 1:
        continue
    p = pp[i + 1]
    ans.append(tuple(sorted((i + 1, p + 1))))
    aa[i], aa[p] = i + 1, a
    pp[i + 1], pp[a] = i, p


print(len(ans))
for a in ans:
    print(*a)