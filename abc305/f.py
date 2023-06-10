from collections import deque

n, m = map(int, input().split())
visited = [False] * (n + 1)
visited[1] = True
trace = deque([1])

for _ in range(2 * n + 1):
    s = input()
    if s == '-1':
        exit()
    elif s == 'OK':
        exit()
    
    k, *v = map(int, s.split())
    nxt = -1
    forward = True
    if n in v:
        nxt = n
    else:
        for x in v:
            if not visited[x]:
                nxt = x
                break
        if nxt == -1:
            trace.pop()
            nxt = trace.pop()
    print(nxt)
    visited[nxt] = True
    trace.append(nxt)