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
ab = [
    list(map(lambda x: int(x) - 1, input().split()))
    for _ in range(m)
]

uf = UnionFind(n)
cnt = [1] * n
x = n * (n - 1) // 2
ans = [x]
for a, b in reversed(ab):
    if uf.is_same(a, b):
        ans.append(ans[-1])
    else:
        ans.append(ans[-1] - cnt[uf.root(a)] * cnt[uf.root(b)])
        s = cnt[uf.root(a)] + cnt[uf.root(b)]
        uf.unite(a, b)
        cnt[uf.root(a)] = s

for x in reversed(ans[:-1]):
    print(x)