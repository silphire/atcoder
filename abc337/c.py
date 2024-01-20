n = int(input())
aa = list(map(int, input().split()))
d = {}
s = set([i + 1 for i in range(n)])
for i, a in enumerate(aa):
    d[a] = i + 1
    s.discard(a)

x = -1
ans = []
while x in d:
    ans.append(x)
    x = d[x]
ans.extend(s)
print(*ans[1:])