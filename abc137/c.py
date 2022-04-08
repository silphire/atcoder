from collections import defaultdict

d = defaultdict(int)
n = int(input())
for _ in range(n):
    s = tuple(sorted(tuple(input().rstrip())))
    d[s] += 1

ans = 0
for _, x in d.items():
    ans += x * (x - 1) // 2

print(ans)