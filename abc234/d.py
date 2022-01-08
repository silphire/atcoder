import heapq

n, k = map(int, input().split())
pp = list(map(int, input().split()))

q = pp[:k]
heapq.heapify(q)
print(q[0])
for x in range(k, n):
    heapq.heappushpop(q, pp[x])
    print(q[0])