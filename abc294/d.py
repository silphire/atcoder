from collections import deque

n, q = map(int, input().split())

nx = 1

que = deque()
s = set()
for i in range(q):
    ee = list(map(int, input().split()))
    if ee[0] == 1:
        que.append(nx)
        nx += 1
    elif ee[0] == 2:
        s.add(ee[1])
    else:
        while True:
            x = que.popleft()
            if x not in s:
                print(x)
                que.appendleft(x)
                break
