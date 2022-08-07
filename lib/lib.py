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
        assert n_vertex >= 0
        if n_vertex == 0:
            return []
            
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
    """プリム法 (最小全域木)
    """
    def __init__(self):
        pass

    def prim(self, edges, start: int, n_vertex: int):
        """プリム法で最小全域木を求めます。
           双方向を前提としています。
        * edges: [(cost, v1, v2)] (0 <= vn < n_vertex)
        * start: 適当に取る点
        * n_vertex: 頂点の数
        """
        import heapq

        assert n_vertex >= 0
        if n_vertex == 0:
            return []

        n = len(edges)
        
        used = [False] * n_vertex
        used[start] = True
        remain = n_vertex - 1
        tree = []
        candidates = [
            (edges[i][0], i)
            for i in range(n)
            if edges[i][1] == start or edges[i][2] == start
        ]
        heapq.heapify(candidates)
        while remain > 0:
            w, i = heapq.heappop(candidates)
            e = edges[i]
            if used[e[1]] and used[e[2]]:
                continue
            tree.append(e)
            for i in range(1, 3):
                if not used[e[i]]:
                    remain -= 1
                    used[e[i]] = True
                    for i, ne in enumerate(edges):
                        if not used[ne[1]] or not used[ne[2]]:
                            heapq.heappush(candidates, (ne[0], i))

        return tree


class Prime(object):
    """素数関係の関数群
    """

    def __init__(self):
        pass

    def prime_sequence(self, n: int):
        """ nまでの素数
        """
        assert n > 0
        
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
        """ nを素因数分解する
        """
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

    MIN = 1
    MAX = -1

    def __init__(self, edges, n_vertex: int, priority: int = MIN):
        from collections import defaultdict

        assert n_vertex > 0

        self.edges = edges
        self.n_vertex = n_vertex
        self.priority = priority

        self.route = defaultdict(list)

        for e in edges:
            w, v1, v2 = e[:3]
            self.route[v1].append((self.priority * w, v2))
            self.route[v2].append((self.priority * w, v1))

    def dijkstra(self, start: int, goal = None):
        """ startで示す頂点からの最短経路を求める
            goal = Noneの場合は全頂点の最短距離を、
            goalに頂点番号が指定された場合はgoalまでの最短経路のみ求める。
        """
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
                return self.priority * w

            for wn, vn in self.route[v]:
                if goal is None:
                    distance[vn] = min(distance[vn], self.priority * (w + wn))
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
        assert size > 0
        self.size = size + 1
        self.arr = [0] * self.size

    def add(self, pos: int, val: int) -> None:
        assert 0 < pos <= self.size

        p = pos
        while p <= self.size:
            self.arr[p] += val
            p += p & -p

    def sum(self, pos: int) -> int:
        assert 0 <= pos <= self.size

        ans = 0
        p = pos
        while p > 0:
            ans += self.arr[p]
            p -= p & -p
        return ans

    def sum_range(self, l: int, r: int) -> int:
        assert 0 < l <= self.size
        assert 0 < r <= self.size
        assert l < r

        return self.sum(r - 1) - self.sum(l - 1)


class RangeBinaryIndexedTree(object):
    """
    Fenwick Tree with multiple addition
    """
    def __init__(self, size: int):
        self.size = size + 1
        self.bit = [BinaryIndexedTree(size) for _ in range(2)]
    
    def add(self, l: int, r: int, val: int) -> None:
        assert 0 < l <= self.size
        assert 0 < r <= self.size
        assert l <= r

        self.bit[0].add(l, -val * (l - 1))
        self.bit[0].add(r, val * (r - 1))
        self.bit[1].add(l, val)
        self.bit[1].add(r, -val)
    
    def sum(self, pos: int) -> int:
        assert 0 < pos <= self.size

        return self.bit[0].sum(pos) + self.bit[1].sum(pos) * pos

    def sum_range(self, l: int, r: int) -> int:
        assert 0 < l <= self.size
        assert 0 < r <= self.size
        assert l < r

        return self.sum(r - 1) - self.sum(l - 1)


def inversion_number(arr):
    """
    転倒数
    arr: [1, ..., n] が入っているリスト
    """
    n = len(arr)
    bit = BinaryIndexedTree(n + 1)
    r = 0
    for i, a in enumerate(arr):
        r += i - bit.sum(a)
        bit.add(a, 1)
    return r


class LCA(object):
    """
    Lowest Common Ancestor
    """
    def __init__(self, size):
        """ 保存領域の初期化。
            辺に重みがついている時の頂点間の重み計算にはcostを使えます。
            size: 頂点の数
        """
        assert size > 0
        self.size = size
        self.graph = [[] for _ in range(size)]
        self.cost_edge = [[] for _ in range(size)]

    def add_edge(self, x: int, y: int, cost: int = 1) -> None:
        """ 木の辺を追加します。
        """
        assert x < self.size
        assert y < self.size

        self.graph[x].append(y)
        self.graph[y].append(x)
        self.cost_edge[x].append(cost)
        self.cost_edge[y].append(cost)
    
    def init(self) -> None:
        """ 全ての辺を追加した後に、LCAを求める為の初期化をする。
        """
        s2 = 1
        while (1 << s2) < self.size:
            s2 += 1
        self.parent = [[-1] * s2 for _ in range(len(self.graph))]
        self.depth = [-1] * self.size
        self.cost_root = [0] * self.size

        def dfs(v, par, d, c) -> None:
            self.parent[v][0] = par
            self.depth[v] = d
            self.cost_root[v] = c
            for e, cc in zip(self.graph[v], self.cost_edge[v]):
                if e != par:
                    dfs(e, v, d + 1, c + cc)
        dfs(0, -1, 0, 0)
        
        for i in range(s2 - 1):
            for j in range(self.size):
                if self.parent[j][i] < 0:
                    self.parent[j][i + 1] = -1
                else:
                    self.parent[j][i + 1] = self.parent[self.parent[j][i]][i]

    def lca(self, x: int, y: int) -> int:
        """ 2つの頂点の最小共通祖先である頂点を返します。
        """
        assert x < self.size
        assert y < self.size

        if self.depth[x] < self.depth[y]:
            x, y = y, x

        s2 = len(self.parent[0])

        for i in range(s2):
            d = self.depth[x] - self.depth[y]
            if (d >> i) & 1 == 1:
                x = self.parent[x][i]
        
        if x == y:
            return x
        
        for i in range(s2 - 1, -1, -1):
            if self.parent[x][i] != self.parent[y][i]:
                x = self.parent[x][i]
                y = self.parent[y][i]
        return self.parent[x][0]

    def dist(self, x: int, y: int) -> int:
        """ 2つの頂点間の距離を返します。
        """
        assert x < self.size
        assert y < self.size

        z = self.lca(x, y)
        return self.depth[x] + self.depth[y] - 2 * self.depth[z]
    
    def cost(self, x: int, y: int) -> int:
        """ 2つの頂点間のコストを返します。
        """
        assert x < self.size
        assert y < self.size

        z = self.lca(x, y)
        return self.cost_root[x] + self.cost_root[y] - 2 * self.cost_root[z]


class ModInt(object):
    def __init__(self, x: int, modulo: int):
        self.__x = x
        self.__modulo = modulo

    def __modret(self, x: int):
        return self.__class__(x % self.__modulo, self.__modulo)

    def __int__(self):
        return self.__x

    def __float__(self):
        return float(self.__x)
    
    def __eq__(self, x: 'ModInt') -> 'ModInt':
        return self.__x == x.__x
    
    def __repr__(self):
        return f'ModInt<{self.__x} mod {self.__modulo}>'

    def modinv(a: int, p: int) -> int:
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

    def __add__(self, x: 'ModInt') -> 'ModInt':
        return self.__modret(self.__x + int(x))

    def __sub__(self, x: 'ModInt') -> 'ModInt':
        y = self.__x - int(x)
        while y < 0:
            y += self.__modulo
        return self.__modret(y)

    def __mul__(self, x: 'ModInt') -> 'ModInt':
        return self.__modret(self.__x * int(x))

    def __truediv__(self, x: 'ModInt') -> 'ModInt':
        return NotImplemented

    def __floordiv__(self, x: 'ModInt') -> 'ModInt':
        if x.__x == 0:
            raise ZeroDivisionError

        inv = self.__class__.modinv(int(x), self.__modulo)
        return self.__modret(self.__x * inv)

    def __mod__(self, x: 'ModInt') -> 'ModInt':
        return self.__modret(int(x))

    def __pow__(self, x: 'ModInt') -> 'ModInt':
        return self.__class__(pow(self.__x, int(x), self.__modulo), self.__modulo)


class MOD(object):
    """ mod K 上の演算ライブラリ
    """
    def __init__(self, modulo: int):
        self.modulo = modulo
        self.size = 2
        self.fact = [1, 1]
        self.inv = [0, 1]
        self.finv = [1, 1]

    def comb(self, n: int, k: int) -> int:
        """ nCk (組み合わせ) を求める
        """
        if n < k or n < 0 or k < 0:
            return 0
        if self.size <= n:
            for i in range(self.size, n + 1):
                self.fact.append(self.fact[-1] * i % self.modulo)
                self.inv.append(self.modulo - self.inv[self.modulo % i] * (self.modulo // i) % self.modulo)
                self.finv.append(self.finv[-1] * self.inv[i] % self.modulo)
            self.size = n
        return self.fact[n] * (self.finv[k] * self.finv[n - k] % self.modulo) % self.modulo

    def hprod(self, n: int, k: int):
        """ nHk (重複組み合わせ) を求める
        """
        return self.comb(n + k - 1, k - 1)

    def modinv(a: int, p: int) -> int:
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

def lcm(a: int, b: int) -> int:
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
    
    def is_orthogonal(x1: int, y1: int, x2: int, y2: int) -> bool:
        """ 線分の直交判定 (ベクトルの内積が0)
            (x1, y1) と (x2, y2) は (0, 0) を基点としたベクトル
        """
        return x1 * x2 + y1 * y2 < 1e-8

    def is_parallel(x1: int, y1: int, x2: int, y2: int) -> bool:
        """ 線分の並行判定 (ベクトルの外積が0)
            (x1, y1) と (x2, y2) は (0, 0) を基点としたベクトル
        """
        return x1 * y2 - x2 * y1 < 1e-8
    
    def triangle_area(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int):
        xa = x1 - x3
        ya = y1 - y3
        xb = x2 - x3
        yb = y2 - y3
        return abs(xa * yb - xb * ya) / 2


    # 点の線分上での存在判定
    def is_on_segment(x1: int, y1: int, x2: int, y2: int, px: int, py: int) -> bool:
        return (x1 <= px <= x2 or x2 <= px <= x1) and (y1 <= py <= y2 or y2 <= py <= y1) and (py * (x1 - x2) + y1 * (x2 - px) + y2 * (px - x1) == 0)


""" 強連結成分分解
    (Strongly Connected Components)
"""
class SCC(object):
    def scc(self, edges, n_vertex):
        """ edges: [(v11, v12), (v21, v22), ...]
        """
        from collections import defaultdict

        gf = defaultdict(set)
        gb = defaultdict(set)
        for v1, v2 in edges:
            gf[v1].add(v2)
            gb[v2].add(v1)

        indexes = [None] * n_vertex
        visited = set()
        x = 0
        def dfs_f(v):
            nonlocal x, visited, indexes, gf

            if v in visited:
                return
            visited.add(v)
            for nv in gf[v]:
                dfs_f(nv)
            indexes[x] = v
            x += 1
        dfs_f(0)

        group = [None] * n_vertex
        x = 0
        def dfs_b(v):
            nonlocal x, group, gb

            if group[v] is not None:
                return
            group[v] = x
            for nv in gb[v]:
                dfs_b(nv)
        for i in reversed(indexes):
            dfs_b(i)
            x += 1
        
        components = defaultdict(list)
        for i, g in enumerate(group):
            components[g].append(i)
        
        return [tuple(c) for g, c in components.items()]

""" 最長増加部分裂 (LIS; Longest Increasing Subsequence)
"""
class LIS(object):
    def __init__(self):
        pass

    def lis(self, xs):
        """ return: LISの長さ
        """
        n = len(xs)
        if n == 0:
            return 0

        import bisect
        dp = [xs[0]]
        for i in range(n):
            if xs[i] > dp[-1]:
                dp.append(xs[i])
            else:
                p = bisect.bisect_left(dp, xs[i])
                dp[p] = xs[i]
        return len(dp)


""" 約数列挙
"""
def divisors(n: int):
    import math
    divs_first = []
    divs_second = []
    for x in range(1, math.floor(n ** 0.5) + 1):
        if n % x == 0:
            divs_first.append(x)
            if x * x != n:
                divs_second.append(n // x)
    divs_first.extend(reversed(divs_second))
    return divs_first


""" AVL木
"""
class Tree(object):
    def __init__(self) -> None:
        self.children = [ None, None ]


class MultiSet(object):
    def __init__(self) -> None:
        pass

    def add(self, x):
        pass

    def lower_bound(self, x):
        pass

    def upper_bound(self, x):
        pass

    def has(self, x) -> bool:
        return False


def cumsum(arr):
    """
    累積和
    """
    n = len(arr)
    cs = [0] * n
    for i in range(n):
        cs[i] = arr[i] + (cs[i - 1] if i > 0 else 0)
    return cs


# パスカルの三角形の計算
# 累積和。左右を操作するやつとか。
# Grundy数
# BITの区間更新
# multiset, ordered set
# AVL木

if __name__ == '__main__':
    pass