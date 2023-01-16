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

index = {}
i = 0
n = int(input())
ss = [None] * n
tt = [None] * n
for j in range(n):
    s, t = input().split()
    ss[j], tt[j] = s, t
    if s not in index:
        index[s] = i
        i += 1
    if t not in index:
        index[t] = i
        i += 1
uf = UnionFind(i + 1)
for s, t in zip(ss, tt):
    if uf.is_same(index[s], index[t]):
        print('No')
        exit()
    uf.unite(index[s], index[t])
print('Yes')