from collections import deque
import heapq

buf = []
add = deque()

q = int(input())
for _ in range(q):
    query = input().rstrip()
    if query == '2':
        if len(buf) > 0:
            print(heapq.heappop(buf))
        else:
            print(add.popleft())
    elif query == '3':
        while add:
            heapq.heappush(buf, add.popleft())
    else:
        x = list(map(int, query.split()))[1]
        add.append(x)