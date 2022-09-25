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


oa = ord('a')
n = int(input())
uf = UnionFind(30)
for i in range(n):
    a, b = input().rstrip().split()
    uf.unite(ord(a) - oa, ord(b) - oa)

s = tuple([uf.root(ord(c) - oa) for c in input().rstrip()])
t = tuple([uf.root(ord(c) - oa) for c in input().rstrip()])
if s == t:
    print('Yes')
else:
    print('No')
