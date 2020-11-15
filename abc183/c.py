import itertools

n, k = map(int, input().split())
t = [
    list(map(int, input().split()))
    for _ in range(n)
]

ans = 0
rr = [a for a in range(2, n + 1)]
for r in itertools.permutations(rr):
    kk = 0
    p = 1
    for x in r + (1,):
        kk += t[p - 1][x - 1]
        p = x
    if kk == k:
        ans += 1
print(ans)