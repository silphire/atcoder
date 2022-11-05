n = int(input())
pp = list(map(int, input().split()))

cc = [a + 1 for a in range(n)]
k = 1
for i in range(n):
    k *= i + 1

x = 0
for i, p in enumerate(pp):
    pos = cc.index(p)
    k //= len(cc)
    x += pos * k
    cc.pop(pos)

x -= 1
pp = []
k = 1
for i in range(n):
    k *= i + 1

cc = [a + 1 for a in range(n)]
while len(pp) < n:
    k //= n - len(pp)
    p = x // k
    pp.append(cc[p])
    x -= p * k
    cc.pop(p)

print(*pp)