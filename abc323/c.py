from collections import Counter

n, m = map(int, input().split())
aa = list(map(int, input().split()))
ss = [
    input()
    for _ in range(n)
]

sc = [0] * n
av = [[] for _ in range(n)]
for i in range(n):
    sc[i] = i + 1
    for j in range(m):
        if ss[i][j] == 'o':
            sc[i] += aa[j]
        else:
            av[i].append(aa[j])
    av[i].sort(reverse=True)
most = sorted(Counter(sc).items())[-1]

ans = [0] * n
for i in range(n):
    if sc[i] == most[0]:
        if most[1] == 1:
            ans[i] = 0
        else:
            ans[i] = 1
    else:
        for x in av[i]:
            sc[i] += x
            ans[i] += 1
            if sc[i] > most[0]:
                break

for a in ans:
    print(a)