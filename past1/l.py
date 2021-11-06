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


class Kruskal(object):
    """
    クラスカル法 (最小全域木)
    """
    def __init__(self):
        pass

    def kruskal(self, edges, n_vertex: int):
        """ edges: (cost, 頂点1, 頂点2) のリスト
            n_vertex: 頂点の最大値
        """

        tree = []
        uf = UnionFind(n_vertex)

        for e in sorted(edges):
            _, v1, v2 = e[:3]
            if uf.is_same(v1, v2):
                continue
            tree.append(e)
            uf.unite(v1, v2)

        return tree


n, m = map(int, input().split())
ttx = [0] * n
tty = [0] * n
ttc = [0] * n
for i in range(n):
    x, y, c = map(int, input().split())
    ttx[i], tty[i], ttc[i] = x, y, c
tsx = [0] * m
tsy = [0] * m
tsc = [0] * m
for i in range(m):
    x, y, c = map(int, input().split())
    tsx[i], tsy[i], tsc[i] = x, y, c

ans = float('inf')
for use in range(1 << m):
    vv = [i for i in range(n)]
    for i in range(m):
        if use & (1 << i) != 0:
            vv.append(100 + i)
    
    nv = len(vv)
    edges = []
    for i in range(nv):
        if vv[i] < 100:
            p = vv[i]
            x1, y1, c1 = ttx[p], tty[p], ttc[p]
        else:
            p = vv[i] - 100
            x1, y1, c1 = tsx[p], tsy[p], tsc[p]
        for j in range(i + 1, nv):
            if vv[j] < 100:
                p = vv[j]
                x2, y2, c2 = ttx[p], tty[p], ttc[p]
            else:
                p = vv[j] - 100
                x2, y2, c2 = tsx[p], tsy[p], tsc[p]
            
            d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            if c1 != c2:
                d *= 10
            edges.append((d, vv[i], vv[j]))
    mst = Kruskal().kruskal(edges, 110)
    ans = min(ans, sum(x[0] for x in mst))
print(ans)