n, k = map(int, input().split())
cc = list(map(int, input().split()))
pp = list(map(int, input().split()))

d = {}
for i in range(n):
    d[cc[i]] = min(d.get(cc[i], 10 ** 10), pp[i])
if len(d) < k:
    print(-1)
else:
    print(sum(sorted(d.values())[:k]))