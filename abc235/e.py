class UnionFind(object):
    """
    Union-Find (Disjoint Set Union)
    """
    def __init__(self, n: int):
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


n, m, q = map(int, input().split())
g = [None] * (m + q)
ans = [False] * q
for i in range(m):
    a, b, c = map(int, input().split())
    g[i] = (c, a, b, None)
for i in range(q):
    a, b, c = map(int, input().split())
    g[m + i] = (c, a, b, i)

uf = UnionFind(n + 1)
g.sort()
for c, a, b, p in g:
    if uf.is_same(a, b):
        if p is not None:
            ans[p] = False
    else:
        if p is None:
            uf.unite(a, b)
        else:
            ans[p] = True

for i in range(q):
    if ans[i]:
        print('Yes')
    else:
        print('No')