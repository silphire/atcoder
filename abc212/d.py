import heapq
q = int(input())
b = []
add = 0
for _ in range(q):
    xx = list(map(int, input().split()))
    if xx[0] == 1:
        heapq.heappush(b, xx[1] - add)
    elif xx[0] == 2:
        add += xx[1]
    else:
        x = heapq.heappop(b)
        print(x + add)
