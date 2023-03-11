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

    def unite(self, x: int, y: int) -> int:
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return rx

        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx

        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        return rx

    def get_size(self, x: int) -> int:
        return self.size[self.root(x)]



n, m = map(int, input().split())
uf = UnionFind(n + 1)
rr = [None] * n
bb = [None] * n
for i in range(m):
    a, b, c, d = input().split()
    a = int(a) - 1
    c = int(c) - 1
    if b == 'R':
        rr[a] = c
    else:
        bb[a] = c
    if d == 'R':
        rr[c] = a
    else:
        bb[c] = a
    uf.unite(a, c)

ax = 0
ay = 0
vis = set()
for x in range(n):
    r = uf.root(x)
    if r in vis:
        continue
    vis.add(r)

    vvis = set()
    v = r
    c = 'R'
    while v is not None and v not in vvis:
        vvis.add(v)
        if c == 'R':
            nv = rr[v]
        else:
            nv = bb[v]
        if nv is None:
            v = None
            break
        if rr[nv] == v:
            c = 'B'
        else:
            c = 'R'
        v = nv
    
    if v is None:
        ay += 1
    else:
        ax += 1

print(*[ax, ay])