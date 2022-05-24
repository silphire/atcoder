import heapq

n, l = map(int, input().split())
aa = list(map(int, input().split()))
sa = sum(aa)

if sa < l:
    aa.append(l - sa)

heapq.heapify(aa)
ans = 0
while len(aa) > 1:
    c1 = heapq.heappop(aa)
    c2 = heapq.heappop(aa)
    ans += c1 + c2
    heapq.heappush(aa, c1 + c2)
print(ans)