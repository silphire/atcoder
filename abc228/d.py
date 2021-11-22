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
        
        return rx
    
    def get_size(self, x: int) -> int:
        return self.size[self.root(x)]

N = 2 ** 20
q = int(input())
uf = UnionFind(N)
a = [-1] * N
rn = {}
for _ in range(q):
    t, x = map(int, input().split())
    if t == 2:
        print(a[x % N])
        continue

    l = x
    r = x
    h = x % N
    if a[h] == -1:
        a[h] = x
        rn[h] = (l, r)
        continue

    while a[h] != -1:
        h = uf.root(h)
        l, r = rn[h]
        rr = (r + 1) % N
        if a[rr] == -1:
            a[rr] = x
            h = uf.unite(h, rr)
            rn[h] = (l, rr)
            break
        else:
            nh = uf.root(rr)
            nl, nr = rn[nh]
            h = uf.unite(h, nh)
            rn[h] = (l, nr)
