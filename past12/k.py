from collections import defaultdict

class UnionFind(object):
    """
    Union-Find (Disjoint Set Union)
    """
    def __init__(self, n: int):
        assert n > 0
        
        self.parent = [x for x in range(n)]
        self.size = [1] * n

    def root(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def is_same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def unite(self, x:int, y: int) -> None:
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return

        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx

        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
    
    def get_size(self, x: int) -> int:
        return self.size[self.root(x)]


g = defaultdict(set)
n, m = map(int, input().split())
aa = [0] * m
bb = [0] * m
for i in range(m):
    aa[i], bb[i] = map(int, input().split())
    g[aa[i]].add(bb[i])
    g[bb[i]].add(aa[i])

q = int(input())
tt = [0] * q
xx = [0] * q
yy = [0] * q
for i in range(q):
    tt[i], xx[i], yy[i] = map(int, input().split())
    if tt[i] == 1:
        g[xx[i]].add(yy[i])
        g[yy[i]].add(xx[i])
    elif tt[i] == 2:
        g[xx[i]].remove(yy[i])
        g[yy[i]].remove(xx[i])

uf = UnionFind(n + 1)
for k, v in g.items():
    for x in v:
        uf.unite(k, x)

ans = []
for i in range(q - 1, -1, -1):
    if tt[i] == 1:
        g[xx[i]].remove(yy[i])
        g[yy[i]].remove(xx[i])
        uf = UnionFind(n + 1)
        for k, v in g.items():
            for x in v:
                uf.unite(k, x)
    elif tt[i] == 2:
        g[xx[i]].add(yy[i])
        g[yy[i]].add(xx[i])
        uf.unite(xx[i], yy[i])
    else:
        ans.append(uf.is_same(xx[i], yy[i]))

for a in reversed(ans):
    if a:
        print('Yes')
    else:
        print('No')