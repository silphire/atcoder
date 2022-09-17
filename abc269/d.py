n = int(input())
xx = [0] * n
yy = [0] * n
for i in range(n):
    xx[i], yy[i] = map(int, input().split())

def conv(x, y):
    return (y + 1000) * 1000 + x + 1000

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

uf = UnionFind(2000 * 2000)
pos = set()
for i in range(n):
    pos.add((xx[i], yy[i]))
cp = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]
for i in range(n):
    for dx, dy in cp:
        if (xx[i] + dx, yy[i] + dy) in pos:
            uf.unite(conv(xx[i], yy[i]), conv(xx[i] + dx, yy[i] + dy))
ans = set()
for i in range(n):
    ans.add(uf.root(conv(xx[i], yy[i])))
print(len(ans))