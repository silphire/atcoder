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


n = int(input())
xx = list(map(lambda x: int(x) - 1, input().split()))
cc = list(map(int, input().split()))
visited = [False] * n

ans = 0
aa = sorted([(-cc[i], i, xx[i]) for i in range(n)])
uf = UnionFind(n)
for i in range(n):
    if uf.is_same(aa[i][1], aa[i][2]):
        ans += cc[aa[i][1]]
    else:
        uf.unite(aa[i][1], aa[i][2])
print(ans)