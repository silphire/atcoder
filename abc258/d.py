n, x = map(int, input().split())
aa = [0] * n
bb = [0] * n
for i in range(n):
    aa[i], bb[i] = map(int, input().split())

inf = float('inf')
ans = inf
minb = inf
ab = 0
for i in range(n):
    if i > x:
        break
    ab += aa[i] + bb[i]
    minb = min(minb, bb[i])
    t = ab + max(0, x - i - 1) * bb[i]
    ans = min(ans, t)
print(ans)