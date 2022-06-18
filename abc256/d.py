n = int(input())
lr = sorted([
    tuple(map(int, input().split()))
    for _ in range(n)
])

ans = []
p = list(lr[0])
for i in range(1, n):
    if p[0] <= lr[i][0] <= p[1]:
        p[1] = max(p[1], lr[i][1])
    else:
        ans.append(p)
        p = list(lr[i])
ans.append(p)

for a in ans:
    print(*a)