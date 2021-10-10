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


class Kruskal(object):
    """
    クラスカル法 (最小全域木)
    """
    def __init__(self):
        pass

    def kruskal(self, edges, n_vertex: int):
        tree = []
        uf = UnionFind(n_vertex)

        for e in sorted(edges):
            _, v1, v2 = e[:3]
            if uf.is_same(v1, v2):
                continue
            tree.append(e)
            uf.unite(v1, v2)

        return tree


class Prim(object):
    def __init__(self):
        pass

    def prim(self, edges, n_vertex: int):
        import heapq
        
        tree = []
        used = [False] * n_vertex
        remain = n_vertex

        v = 0
        while remain > 0:
            pass

        return tree


class Prime(object):
    def __init__(self):
        pass

    def prime_sequence(self, n: int):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        upper_bound = int(n ** 0.5) + 1
        for i in range(2, upper_bound):
            if not primes[i]:
                continue
            for j in range(2 * i, n + 1, i):
                primes[j] = False
        return [i for i in range(2, n + 1) if primes[i]]

    def prime_factorize(self, n: int):
        spf = [1] * (n + 1)
        spf[0] = 0
        for i in range(2, n + 1):
            if spf[i] != 1:
                continue
            for j in range(i, n + 1, i):
                spf[j] = i

        f = []
        while n > 1:
            s = spf[n]
            f.append(s)
            n //= s
        return f


class Dijkstra(object):
    """
    * edges: [(weight, vertex_1, vertex_2)]
    """

    def __init__(self, edges, n_vertex: int):
        from collections import defaultdict

        assert n_vertex > 0

        self.edges = edges
        self.n_vertex = n_vertex

        self.route = defaultdict(list)

        for e in edges:
            w, v1, v2 = e[:3]
            self.route[v1].append((-w, v2))
            self.route[v2].append((-w, v1))

    def dijkstra(self, start: int, goal = None):
        import heapq

        assert start < self.n_vertex
        assert goal is None or goal < self.n_vertex

        visited = [False] * self.n_vertex
        if goal is None:
            distance = [float('inf')] * self.n_vertex
            distance[start] = 0

        q = [(0, start)]
        while q:
            w, v = heapq.heappop(q)
            if visited[v]:
                continue
            visited[v] = True

            if goal is not None and v == goal:
                return -w

            for wn, vn in self.route[v]:
                if goal is None:
                    distance[vn] = min(distance[vn], -(w + wn))
                elif vn == goal:
                    return -(w + wn)
                heapq.heappush(q, (w + wn, vn))

        if goal is None:
            return distance
        else:
            return float('inf')


class MaxFlow(object):
    """
    Dinic法
    """
    def __init__(self):
        pass


class SegmentTree(object):
    """
    セグメント木
    """
    def __init__(self):
        pass


class BinaryIndexedTree(object):
    """
    Fenwick Tree
    """
    def __init__(self, size: int):
        self.size = size + 1
        self.arr = [0] * self.size

    def add(self, pos: int, val: int):
        assert 0 < pos <= self.size

        p = pos
        while p <= self.size:
            self.arr[p] += val
            p += p & -p

    def sum(self, pos: int):
        assert 0 < pos <= self.size

        ans = 0
        p = pos
        while p > 0:
            ans += self.arr[p]
            p -= p & -p
        return ans


class LCA(object):
    """
    Lowest Common Ancestor
    """
    def __init__(self):
        pass

    def lca(x: int, y: int):
        pass

    def dist(x: int, y: int):
        pass

    def dfs(x: int):
        pass


class MOD(object):
    def __init__(self, modulo: int):
        self.modulo = modulo
        self.size = 2
        self.fact = [1, 1]
        self.inv = [1, 1]
        self.finv = [0, 1]
    
    def comb(self, n: int, k: int):
        if n < k or n < 0 or k < 0:
            return 0
        if self.size < n:
            for i in range(self.size, n + 1):
                self.fact.append(self.fact[-1] * i % self.modulo)
                self.inv.append(self.modulo - self.inv[self.modulo % i] * (self.modulo // i) % self.modulo)
                self.finv.append(self.finv[-1] * self.inv[i] % self.modulo)
            self.size = n
        return self.fact[n] * (self.finv[k] * self.finv[n - k] % self.modulo) % self.modulo
    
    def modinv(a: int, p: int):
        """ mod pとした時のaの逆元
        """
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

def lcm(a, b):
    """ 最小公倍数
    """
    import math

    if b == 0:
        return a
    else:
        return math.gcd(b, a % b)


""" 幾何ライブラリ
"""
class Geometry(object):
    def rotate(x, y, theta):
        """回転行列
        """
        import math
        return (
            math.cos(theta) * x - math.sin(theta) * y,
            math.sin(theta) * x + math.cos(theta) * y,
        )
    
    # 線分の直交判定 (ベクトルの内積が0)
    def is_orthogonal(x1: int, y1: int, x2: int, y2: int) -> bool:
        return x1 * x2 + y1 * y2 < 1e-8

    # 線分の並行判定 (ベクトルの外積が0)
    # 点の線分上での存在判定


# scipy.special.comb(n, r)
# パスカルの三角形の計算
# 累積和。左右を操作するやつとか。
# Grundy数

if __name__ == '__main__':
    pass