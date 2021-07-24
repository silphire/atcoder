from collections import defaultdict
MOD = 10 ** 9 + 7
n, m = map(int, input().split())
mint = [float('inf')] * n
minn = [0] * n
g = defaultdict(set)
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].add(b)
    g[b].add(a)

q = {0}
t = 0
ans = 0
minn[0] = 1
while q:
    t += 1
    nq = set()
    for x in q:
        for y in g[x]:
            if t < mint[y]:
                mint[y] = t
                minn[y] = minn[x] % MOD
                nq.add(y)
            elif t == mint[y]:
                minn[y] += minn[x]
                minn[y] %= MOD
                nq.add(y)
    q = nq
    if (n - 1) in q:
        print(minn[n - 1] % MOD)
        exit()
print(0)