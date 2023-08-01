import heapq

n, d = map(int, input().split())
work = [None] * n
for i in range(n):
    x, y = map(int, input().split())
    work[i] = (x, -y)
heapq.heapify(work)

ans = 0
cd = 1
while work and cd <= d:
    x, y = heapq.heappop(work)
    if x > d:
        break
    ans -= y
    if x > cd:
        cd = x
    cd += 1
print(ans)