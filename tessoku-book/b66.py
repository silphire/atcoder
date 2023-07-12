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

n, m = map(int, input().split())
ab = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
q = int(input())
qq = [tuple(map(int, input().split())) for _ in  range(q)]
uf = UnionFind(n)
ss = set()
for op, *arg in qq:
    if op == 1:
        ss.add(arg[0])
for i in range(m):
    if i + 1 not in ss:
        uf.unite(*ab[i])
ans = []
for op, *arg in reversed(qq):
    if op == 1:
        uf.unite(*ab[arg[0] - 1])
    else:
        ans.append(uf.is_same(arg[0] - 1, arg[1] - 1))

for a in reversed(ans):
    if a:
        print('Yes')
    else:
        print('No')
