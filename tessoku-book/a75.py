n = int(input())
td = sorted([
    tuple(map(int, input().split()))
    for _ in range(n)
], key=lambda x: (x[1], x[1]-x[0]))

ans = 0
s = 0
for t, d in td:
    if s + t <= d:
        ans += 1
        s += t
print(ans)