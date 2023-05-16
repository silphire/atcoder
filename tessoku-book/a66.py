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

n, q = map(int, input().split())
uf = UnionFind(n + 1)
for _ in range(q):
    op, u, v = map(int, input().split())
    if op == 1:
        uf.unite(u, v)
    else:
        print(['No', 'Yes'][int(uf.is_same(u, v))])
