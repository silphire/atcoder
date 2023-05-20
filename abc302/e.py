n, q = map(int, input().split())
pt = [set() for _ in range(n)]
npt = [0] * n
ans = n
for _ in range(q):
    op, *uv = map(lambda x: int(x) - 1, input().split())
    if op == 0:
        u, v = uv

        if npt[u] == 0:
            ans -= 1
        npt[u] += 1
        pt[u].add(v)
            
        if npt[v] == 0:
            ans -= 1
        npt[v] += 1
        pt[v].add(u)
    else:
        v = uv[0]
        for p in pt[v]:
            pt[p].discard(v)
            npt[p] -= 1
            if npt[p] == 0:
                ans += 1
        if npt[v] > 0:
            ans += 1
            npt[v] = 0
        pt[v] = set()
    print(ans)