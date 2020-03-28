import heapq

x, y, a, b, c = map(int, input().split())
pp = list(map(lambda x: (-int(x), 1), input().split()))
qq = list(map(lambda x: (-int(x), 2), input().split()))
rr = list(map(lambda x: (-int(x), 3), input().split()))

xx = pp + qq + rr
heapq.heapify(xx)
t = x + y
ans = 0
for _ in range(t):
    while len(xx) > 0:
        v = heapq.heappop(xx)
        if v[1] == 1 and x <= 0:
            continue
        if v[1] == 2 and y <= 0:
            continue
        break

    if v[1] == 1:
        x -= 1
    if v[1] == 2:
        y -= 1
    ans += v[0]

print(-ans)
