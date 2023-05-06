import heapq

hq = []
q = int(input())
for _ in range(q):
    op, *arg = map(int, input().split())
    if op == 1:
        heapq.heappush(hq, arg[0])
    elif op == 2:
        print(hq[0])
    else:
        heapq.heappop(hq)