class UnionFind(object):
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
s = []
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < 0:
        uf.unite(a, b)
    else:
        s.append((c, a, b))
s.sort()
ans = 0
for c, a, b in s:
    if uf.is_same(a, b):
        ans += c
    else:
        uf.unite(a, b)
print(ans)