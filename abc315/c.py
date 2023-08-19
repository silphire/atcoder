from collections import defaultdict
ls = defaultdict(list)
n = int(input())
fs = sorted([
    tuple(map(int, input().split()))
    for _ in range(n)
], key=lambda x: (-x[1], x[0]))

for (f, s) in fs:
    ls[f].append(s)

top = sorted([v[0] for v in ls.values()], reverse=True)

ans = 0
if len(top) >= 2:
    ans = top[0] + top[1]
for f, ss in ls.items():
    if len(ss) >= 2:
        ans = max(ans, ss[0] + ss[1] // 2)
print(ans)