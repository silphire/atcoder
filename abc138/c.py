import heapq

n = int(input())
v = list(map(int, input().split()))

heapq.heapify(v)
while len(v) > 1:
    v1 = heapq.heappop(v)
    v2 = heapq.heappop(v)
    heapq.heappush(v, (v1 + v2) / 2)
print(v[0])
