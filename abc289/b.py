from collections import defaultdict

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
aa = list(map(int, input().split()))
uf = UnionFind(n + 1)

for a in aa:
    uf.unite(a, a + 1)

d = defaultdict(list)
for i in range(1, n + 1):
    d[uf.root(i)].append(i)

ans = []
visited = [False] * (n + 1)
for i in range(1, n + 1):
    if not visited[i]:
        for x in sorted(d[uf.root(i)], reverse=True):
            ans.append(x)
            visited[x] = True
print(*ans)