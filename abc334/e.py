class UnionFind(object):
    """
    Union-Find (Disjoint Set Union)
    """
    def __init__(self, n: int):
        assert n > 0

        self.parent = list(range(n))
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


def modinv(a: int, p: int) -> int:
    """ mod pとした時のaの逆元
    """
    import math
    assert math.gcd(a, p) == 1

    b = p
    u = 1
    v = 0
    while b > 0:
        t = a // b

        a -= t * b
        a, b = b, a

        u -= t * v
        u, v = v, u

    u %= p
    if u < 0:
        u += p
    return u


h, w = map(int, input().split())
ss = [
    input()
    for _ in range(h)
]

uf = UnionFind(h * w)

def pos(a, b):
    return a + b * w

for y in range(h):
    for x in range(w):
        if ss[y][x] == '.':
            continue

        p = x + y * w

        if x - 1 >= 0 and ss[y][x - 1] == '#':
            q = pos(x - 1, y)
            uf.unite(p, q)
        if x + 1 < w and ss[y][x + 1] == '#':
            q = pos(x + 1, y)
            uf.unite(p, q)
        if y - 1 >= 0 and ss[y - 1][x] == '#':
            q = pos(x, y - 1)
            uf.unite(p, q)
        if y + 1 < h and ss[y + 1][x] == '#':
            q = pos(x, y + 1)
            uf.unite(p, q)

rs = set()
nr = 0
for y in range(h):
    for x in range(w):
        if ss[y][x] == '.':
            nr += 1
        else:
            rs.add(uf.root(pos(x, y)))
nregion = len(rs)

total = 0
for y in range(h):
    for x in range(w):
        if ss[y][x] == '#':
            continue
        rs = set()

        if x - 1 >= 0 and ss[y][x - 1] == '#':
            q = pos(x - 1, y)
            rs.add(uf.root(q))
        if x + 1 < w and ss[y][x + 1] == '#':
            q = pos(x + 1, y)
            rs.add(uf.root(q))
        if y - 1 >= 0 and ss[y - 1][x] == '#':
            q = pos(x, y - 1)
            rs.add(uf.root(q))
        if y + 1 < h and ss[y + 1][x] == '#':
            q = pos(x, y + 1)
            rs.add(uf.root(q))

        total += nregion - len(rs) + 1

MOD = 998244353
print(total * modinv(nr, MOD) % MOD)
