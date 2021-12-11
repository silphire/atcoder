from collections import Counter

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
if m == 0:
    print('Yes')
    exit()
aa = [None] * m
bb = [None] * m
for i in range(m):
    aa[i], bb[i] = map(int, input().split())
c1 = Counter(aa + bb)
if max(c1.values()) > 2:
    print('No')
    exit()

uf = UnionFind(n + 1)
for a, b in zip(aa, bb):
    if uf.root(a) == uf.root(b):
        print('No')
        exit()
    uf.unite(a, b)
print('Yes')

