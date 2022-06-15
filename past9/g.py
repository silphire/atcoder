from collections import deque

n, q = map(int, input().split())
gr = [[False] * n for _ in range(n)]

for i in range(q):
    x, u, v = map(int, input().split())
    u -= 1
    v -= 1
    if x == 1:
        gr[u][v] = not gr[u][v]
        gr[v][u] = not gr[v][u]
    else:
        visited = [False] * n
        q = deque([u])
        f = False
        while q:
            a = q.popleft()
            if a == v:
                f = True
                break
            visited[a] = True
            for b in range(n):
                if gr[a][b] and not visited[b]:
                    q.append(b)
        if f:
            print('Yes')
        else:
            print('No')