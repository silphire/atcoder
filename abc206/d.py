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


n = int(input())
aa = list(map(int, input().split()))
aas = set(aa)
d = {a:i for i, a in enumerate(aas)}
uf = UnionFind(len(aas))

ans = 0
for i in range(n // 2):
    if i == n - i - 1:
        continue
    if aa[i] != aa[n - i - 1]:
        x = d[aa[i]]
        y = d[aa[n - i - 1]]
        if not uf.is_same(x, y):
            uf.unite(x, y)
            ans += 1
print(ans)