import heapq

n, k = map(int, input().split())
aa = list(map(int, input().split()))
si = sum(aa[:k])

t = 0
s = []
for i, a in enumerate(aa):
    if len(s) < k:
        t += a
        heapq.heappush(s, (a, i))
    elif s[0][0] < a:
        t += a - s[0][0]
        heapq.heappushpop(s, (a, i))
    if t > si:
        print(sum([ss[1] for ss in s]) - k * (k - 1) // 2)
        exit()
print(-1)