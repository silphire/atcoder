n = int(input())
p = list(map(int, input().split()))

f = [False] * 200001

ex = set()
ans = 0
for i in range(n):
    f[p[i]] = True
    while f[ans]:
        ans += 1
    print(ans)
