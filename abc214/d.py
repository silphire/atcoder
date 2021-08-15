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
    
    def get_size(self, x: int) -> int:
        return self.size[self.root(x)]

n = int(input())
e = [None] * (n - 1)
for i in range(n - 1):
    u, v, w = map(int, input().split())
    e[i] = (w, u - 1, v - 1)
e.sort()

ans = 0
uf = UnionFind(n)
for w, u, v in e:
    ans += w * uf.get_size(u) * uf.get_size(v)
    uf.unite(u, v)
print(ans)