class UnionFind(object):
    """
    Union-Find (Disjoint Set Union)
    """
    def __init__(self, n: int):
        assert n > 0

        self.parent = list(range(n))
        self.size = [1] * n

    def root(self, x: int) -> int:
        """
        xの根となるノードの番号を取得
        """
        if self.parent[x] != x:
            self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def is_same(self, x: int, y: int) -> bool:
        """
        xとyの根が同じかどうか
        """
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int) -> int:
        """
        xとyを同じ根を持つようにする
        """
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
        """
        xで指定する頂点の配下にある頂点の数を返す
        """
        return self.size[self.root(x)]


from collections import defaultdict

n, m = map(int, input().split())

v = []
uf = UnionFind(n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    v.append((a, b))
    uf.unite(a, b)

d = defaultdict(int)
for es in v:
    d[uf.root(es[0])] += 1

ans = 0
for r, x in d.items():
    s = uf.get_size(r)
    ans += s * (s - 1) // 2 - d[r]
print(ans)