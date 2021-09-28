from collections import defaultdict

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


n, m = map(int, input().split())
uf = UnionFind(n + 1)
pp = list(map(int, input().split()))
for _ in range(m):
    x, y = map(int, input().split())
    uf.unite(x, y)

ans = 0
for i in range(1, n + 1):
    if uf.root(i) == uf.root(pp[i - 1]):
        ans += 1
print(ans)