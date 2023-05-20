import itertools

n, m = map(int, input().split())
ss = [
    input()
    for _ in range(n)
]

sc = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        diff = 0
        for k in range(m):
            if ss[i][k] != ss[j][k]:
                diff += 1
        sc[i][j] = sc[j][i] = diff

for pp in itertools.permutations([x for x in range(n)], n):
    f = True
    for i in range(n - 1):
        if sc[pp[i]][pp[i + 1]] != 1:
            f = False
            break
    if f:
        print('Yes')
        exit()
print('No')