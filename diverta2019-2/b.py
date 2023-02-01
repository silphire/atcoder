from collections import defaultdict

n = int(input())
if n == 1:
    print(1)
    exit()

pp = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

d = defaultdict(int)
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        dx = pp[i][0] - pp[j][0]
        dy = pp[i][1] - pp[j][1]
        d[(dx, dy)] += 1

ps = set(pp)

ans = 10 ** 10
for (dx, dy) in d:
    s = 0
    for (x, y) in pp:
        if (x + dx, y + dy) not in ps:
            s += 1
    ans = min(ans, s)
print(ans)
