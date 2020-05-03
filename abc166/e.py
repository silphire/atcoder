from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
ap = defaultdict(int)
for i in range(n):
    ap[i - a[i]] += 1

ans = 0
for i in range(n):
    ans += ap[a[i] + i]
print(ans)