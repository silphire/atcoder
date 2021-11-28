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
    
    def get_size(self, x: int) -> int:
        return self.size[self.root(x)]


n, m = map(int, input().split())
ab = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ab[a].append(b)
uf = UnionFind(n)

ans = [0] * n
for a in range(n - 1, 0, -1):
    ans[a - 1] = ans[a] + 1
    for b in ab[a]:
        if uf.root(a) != uf.root(b):
            uf.unite(a, b)
            ans[a - 1] -= 1
for a in ans:
    print(a)