import heapq

n, k = map(int, input().split())
aa = list(map(int, input().split()))
h = [(-a, a, 1, i) for i, a in enumerate(aa)]
heapq.heapify(h)
ans = [0] * n
while k > 0:
    v, a, x, p = heapq.heappop(h)
    ans[p] += 1
    x += 1
    heapq.heappush(h, (-a / x, a, x, p))
    k -= 1
print(*ans)