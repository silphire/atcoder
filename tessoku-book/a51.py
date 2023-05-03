from collections import deque

que = deque()
q = int(input())
for _ in range(q):
    op, *arg = input().split()
    op = int(op)
    if op == 1:
        que.appendleft(arg[0])
    elif op == 2:
        x = que.popleft()
        que.appendleft(x)
        print(x)
    else:
        que.popleft()