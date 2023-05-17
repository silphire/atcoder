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

ee = [None] * m
for i in range(m):
    a, b, c = map(int, input().split())
    ee[i] = (c, a, b)
ee.sort()

ans = 0
for i in range(m):
    c, a, b = ee[i]
    if not uf.is_same(a, b):
        uf.unite(a, b)
        ans += c
print(ans)