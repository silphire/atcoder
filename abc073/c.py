from collections import defaultdict

c = defaultdict(int)

n = int(input())
for i in range(n):
    x = int(input())
    c[x] += 1
ans = 0
for k, v in c.items():
    if v % 2 == 1:
        ans += 1
print(ans)