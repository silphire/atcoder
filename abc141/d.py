import heapq

n, m = map(int, input().split())
aa = list(map(int, input().split()))

h = [-a for a in aa]
heapq.heapify(h)
for _ in range(m):
    x = h[0]
    heapq.heapreplace(h, -(-x // 2))

print(sum([-hh for hh in h]))