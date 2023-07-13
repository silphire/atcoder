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


class Kruskal(object):
    """
    クラスカル法 (最小全域木)
    """
    def __init__(self):
        pass

    def kruskal(self, edges, n_vertex: int):
        assert n_vertex >= 0
        if n_vertex == 0:
            return []

        tree = []
        uf = UnionFind(n_vertex)

        for e in sorted(edges):
            _, v1, v2 = e[:3]
            if uf.is_same(v1, v2):
                continue
            tree.append(e)
            uf.unite(v1, v2)

        return tree

n, m = map(int, input().split())
ee = []
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    ee.append((-c, a, b))
g = Kruskal().kruskal(ee, n)
print(-sum([c for c, a, b in g]))