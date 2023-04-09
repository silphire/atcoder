import heapq

n, k = map(int, input().split())
aa = list(map(int, input().split()))
q = [0]
px = float('inf')
k += 1
while k > 0:
    while True:
        x = heapq.heappop(q)
        if x != px:
            px = x
            break
    for a in aa:
        heapq.heappush(q, x + a)
    k -= 1
print(x)