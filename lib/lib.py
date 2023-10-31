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


class Kruskal(object):
    """
    クラスカル法 (最小全域木)
    """
    def __init__(self) -> None:
        pass

    def kruskal(
            self,
            edges: list[tuple[int, int, int]],
            n_vertex: int
    ) -> list[tuple[int, int, int]]:
        """ クラスカル法で最小全域木を求める
            edges: (cost, vertex_1, vertex_2)
            コストの小さい辺から採用していく
        """
        assert n_vertex > 0

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
    def __init__(self) -> None:
        pass

    def prim(
        self,
        edges: list[tuple[int, int, int]],
        start: int,
        n_vertex: int,
    ) -> list[tuple[int, int, int]]:
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

    def __init__(self) -> None:
        pass

    def prime_sequence(self, n: int) -> list[int]:
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

    def prime_factorize(self, n: int) -> list[int]:
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

    from enum import Enum

    class Priority(Enum):
        MIN = 1
        MAX = -1

    def __init__(
            self,
            edges: list[tuple[int, int, int]],
            n_vertex: int,
            priority: int = Priority.MIN
    ):
        from collections import defaultdict

        assert n_vertex > 0

        self.edges = edges
        self.n_vertex = n_vertex
        self.priority = priority

        self.route: dict[int, list[tuple[int, int]]] = defaultdict(list)

        for e in edges:
            w, v1, v2 = e[:3]
            assert w >= 0
            self.route[v1].append((self.priority * w, v2))
            self.route[v2].append((self.priority * w, v1))

    def dijkstra(self, start: int, goal: int) -> int:
        """ startで示す頂点からgoalで示す頂点までの最短経路を求める
        """
        import heapq
        import sys

        assert 0 <= start < self.n_vertex
        assert 0 <= goal < self.n_vertex

        visited = [False] * self.n_vertex

        q: list[tuple[int, int]] = [(0, start)]
        while q:
            w, v = heapq.heappop(q)
            if visited[v]:
                continue
            visited[v] = True

            if v == goal:
                return self.priority * w

            for wn, vn in self.route[v]:
                heapq.heappush(q, (w + wn, vn))

        return self.priority * sys.maxsize

    def dijkstra_all_dests(self, start: int) -> list[int]:
        """ startで示す頂点から全頂点への最短経路を求める
        """
        import heapq
        import sys

        assert start < self.n_vertex

        visited: list[bool] = [False] * self.n_vertex
        distance: list[int] = [sys.maxsize] * self.n_vertex
        distance[start] = 0

        q: list[tuple[int, int]] = [(0, start)]
        while q:
            w, v = heapq.heappop(q)
            if visited[v]:
                continue
            visited[v] = True

            for wn, vn in self.route[v]:
                distance[vn] = min(distance[vn], self.priority * (w + wn))
                heapq.heappush(q, (w + wn, vn))

        return distance

    def dijkstra_with_route(
            self,
            start: int,
            goal: int
    ) -> tuple[int, list[int]]:
        """ startで示す頂点からgoalで示す頂点までの最短経路の距離とその経路を求める
        """
        import heapq
        import sys

        assert start < self.n_vertex
        assert goal < self.n_vertex

        visited: list[bool] = [False] * self.n_vertex
        prev: list[int | None] = [None] * self.n_vertex

        q: list[tuple[int, int, int | None]] = [(0, start, None)]
        while q:
            w, v, p = heapq.heappop(q)
            if visited[v]:
                continue
            visited[v] = True
            prev[v] = p

            if v == goal:
                r = []
                while v is not None:
                    r.append(v)
                    v = prev[v]
                return self.priority * w, r[::-1]

            for wn, vn in self.route[v]:
                heapq.heappush(q, (w + wn, vn, v))

        return self.priority * sys.maxsize, []


class MaxFlow(object):
    """
    ford-fulkerson法
    TODO Dinic法

    * edges: [(weight, vertex_1, vertex_2)]
    """
    def __init__(self, edges: list[tuple[int, int, int]]):
        pass

    def flow(self, start: int) -> int:
        return -1


class SegmentTree(object):
    """
    セグメント木
    """
    from collections.abc import Callable

    def __init__(self, arr: list[int], e: int, op: Callable[[int, int], int]):
        """
            arr: 初期値
            e: 単位元
            op: 二項演算
        """
        n = len(arr)
        self.p2 = 1 << n.bit_length()
        if self.p2 < n:
            self.p2 += 1

        self.n = n
        self.e = e
        self.op = op

        self.buf = [e] * (self.p2 * 2)
        for i in range(n):
            self.buf[self.p2 + i] = arr[i]
        for i in range(self.p2 - 1, -1, -1):
            self.buf[i] = op(self.buf[2 * i], self.buf[2 * i + 1])

    def set(self, i: int, x: int) -> None:
        """ i の位置を x に置き換える
        """
        assert 0 <= i < self.n

        i += self.p2
        self.buf[i] = x
        while i > 1:
            self.buf[i >> 1] = self.op(self.buf[i], self.buf[i ^ 1])
            i >>= 1

    def get(self, p: int, q: int) -> int:
        """ [p, q) に op を適用した結果を返す
        """
        assert 0 <= p <= self.n
        assert 0 <= q <= self.n
        assert p < q

        x = self.e

        p += self.p2
        q += self.p2
        while p < q:
            if p & 1:
                x = self.op(x, self.buf[p])
                p += 1
            if q & 1:
                x = self.op(x, self.buf[q - 1])
            p >>= 1
            q >>= 1

        return x

    # TODO セグメント木の上での二分探索
    def leftmost(self, x: int, f: Callable[[int], bool]) -> int:
        return 0

    # TODO セグメント木の上での二分探索
    def rightmost(self, x: int, f: Callable[[int], bool]) -> int:
        return 0

    @staticmethod
    def rmq(arr: list[int]) -> 'SegmentTree':
        """ Range Minimum Query
        """
        import sys
        return SegmentTree(arr, sys.maxsize, lambda x, y: min(x, y))

    @staticmethod
    def raq(arr: list[int]) -> 'SegmentTree':
        """ Range Add Query
        """
        return SegmentTree(arr, 0, lambda x, y: x + y)


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
        while p < self.size:
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

    def sum_range(self, left: int, right: int) -> int:
        assert 0 < left <= self.size
        assert 0 < right <= self.size
        assert left < right

        return self.sum(right - 1) - self.sum(left - 1)

    def get(self, pos: int) -> int:
        assert 0 < pos <= self.size
        return self.sum_range(pos, pos + 1)


class RangeBinaryIndexedTree(object):
    """
    Fenwick Tree with multiple addition
    """
    def __init__(self, size: int):
        self.size = size + 1
        self.bit = [BinaryIndexedTree(size) for _ in range(2)]

    def add(self, left: int, right: int, val: int) -> None:
        assert 0 < left <= self.size
        assert 0 < right <= self.size
        assert left <= right

        self.bit[0].add(left, -val * (left - 1))
        self.bit[0].add(right, val * (right - 1))
        self.bit[1].add(left, val)
        self.bit[1].add(right, -val)

    def sum(self, pos: int) -> int:
        assert 0 < pos <= self.size

        return self.bit[0].sum(pos) + self.bit[1].sum(pos) * pos

    def sum_range(self, left: int, right: int) -> int:
        assert 0 < left <= self.size
        assert 0 < right <= self.size
        assert left < right

        return self.sum(right - 1) - self.sum(left - 1)

    def get(self, pos: int) -> int:
        assert 0 < pos <= self.size
        return self.sum_range(pos, pos + 1)


def inversion_number(arr: list[int]) -> int:
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
    def __init__(self, size: int) -> None:
        """ 保存領域の初期化。
            辺に重みがついている時の頂点間の重み計算にはcostを使えます。
            size: 頂点の数
        """
        assert size > 0
        self.size = size
        self.graph: list[list[int]] = [[] for _ in range(size)]
        self.cost_edge: list[list[int]] = [[] for _ in range(size)]

    def add_edge(self, x: int, y: int, cost: int = 1) -> None:
        """ 木の辺を追加します。
        """
        assert 0 <= x < self.size
        assert 0 <= y < self.size

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

        def dfs(v: int, par: int, d: int, c: int) -> None:
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
        assert 0 <= x < self.size
        assert 0 <= y < self.size

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
        assert 0 <= x < self.size
        assert 0 <= y < self.size

        z = self.lca(x, y)
        return self.depth[x] + self.depth[y] - 2 * self.depth[z]

    def cost(self, x: int, y: int) -> int:
        """ 2つの頂点間のコストを返します。
        """
        assert 0 <= x < self.size
        assert 0 <= y < self.size

        z = self.lca(x, y)
        return self.cost_root[x] + self.cost_root[y] - 2 * self.cost_root[z]


class ModInt(object):
    def __init__(self, x: int, modulo: int):
        assert modulo != 0

        self.__x = x
        self.__modulo = modulo

    def __modret(self, x: int) -> 'ModInt':
        return self.__class__(x % self.__modulo, self.__modulo)

    def __int__(self) -> int:
        return self.__x

    def __float__(self) -> float:
        return float(self.__x)

    def __eq__(self, x: 'ModInt') -> bool:
        if not isinstance(x, ModInt):
            return NotImplemented
        return self.__x == x.__x

    def __repr__(self) -> str:
        return f'ModInt<{self.__x} mod {self.__modulo}>'

    @staticmethod
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
        return self.__class__(
            pow(self.__x, int(x), self.__modulo),
            self.__modulo
        )


class MOD(object):
    """ mod K 上の演算ライブラリ
    """
    def __init__(self, modulo: int):
        assert modulo > 0

        self.modulo = modulo
        self.size = 2
        self.fact = [1, 1]
        self.inv = [0, 1]
        self.finv = [1, 1]

    def comb(self, n: int, k: int) -> int:
        """ nCk (組み合わせ) を求める
        """
        import math
        if hasattr(math, 'comb'):
            return math.comb(n, k)

        if n < k or n < 0 or k < 0:
            return 0
        m = self.modulo
        if self.size <= n:
            for i in range(self.size, n + 1):
                self.fact.append(self.fact[-1] * i % m)
                self.inv.append(m - self.inv[m % i] * (self.modulo // i) % m)
                self.finv.append(self.finv[-1] * self.inv[i] % m)
            self.size = n
        return self.fact[n] * (self.finv[k] * self.finv[n - k] % m) % m

    def hprod(self, n: int, k: int) -> int:
        """ nHk (重複組み合わせ) を求める
        """
        return self.comb(n + k - 1, k - 1)

    @staticmethod
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


def lcm(a: int, b: int) -> int:
    """ 最小公倍数
    """
    import math

    if hasattr(math, 'lcm'):
        return math.lcm(a, b)

    if a == 0 or b == 0:
        return 0

    return a * b // math.gcd(b, a % b)


class Geometry(object):
    """ 幾何ライブラリ
    """

    @staticmethod
    def rotate(x: float, y: float, theta: float) -> tuple[float, float]:
        """回転行列
        """
        import math
        return (
            math.cos(theta) * x - math.sin(theta) * y,
            math.sin(theta) * x + math.cos(theta) * y,
        )

    @staticmethod
    def is_orthogonal(x1: int, y1: int, x2: int, y2: int) -> bool:
        """ 線分の直交判定 (ベクトルの内積が0)
            (x1, y1) と (x2, y2) は (0, 0) を基点としたベクトル
        """
        return x1 * x2 + y1 * y2 < 1e-8

    @staticmethod
    def is_parallel(x1: int, y1: int, x2: int, y2: int) -> bool:
        """ 線分の並行判定 (ベクトルの外積が0)
            (x1, y1) と (x2, y2) は (0, 0) を基点としたベクトル
        """
        return x1 * y2 - x2 * y1 < 1e-8

    @staticmethod
    def triangle_area(
        x1: int, y1: int,
        x2: int, y2: int,
        x3: int, y3: int,
    ) -> float:
        xa = x1 - x3
        ya = y1 - y3
        xb = x2 - x3
        yb = y2 - y3
        return abs(xa * yb - xb * ya) / 2

    @staticmethod
    def is_on_segment(
        x1: int, y1: int,
        x2: int, y2: int,
        px: int, py: int
    ) -> bool:
        """点の線分上での存在判定
        """
        return (
            (x1 <= px <= x2 or x2 <= px <= x1)
            and (y1 <= py <= y2 or y2 <= py <= y1)
            and (py * (x1 - x2) + y1 * (x2 - px) + y2 * (px - x1) == 0)
        )


class SCC(object):
    """ 強連結成分分解
        (Strongly Connected Components)
    """

    def scc(
            self,
            edges: list[tuple[int, int]],
            n_vertex: int
    ) -> list[tuple[int, ...]]:
        """ edges: [(v11, v12), (v21, v22), ...]
        """
        from collections import defaultdict

        gf = defaultdict(set)
        gb = defaultdict(set)
        for v1, v2 in edges:
            gf[v1].add(v2)
            gb[v2].add(v1)

        indexes = [-1] * n_vertex
        visited = [False] * n_vertex
        x = 0

        def dfs_f(v: int) -> None:
            nonlocal x, visited, indexes, gf

            if visited[v]:
                return
            visited[v] = True
            for nv in gf[v]:
                dfs_f(nv)
            indexes[x] = v
            x += 1
        for v in range(n_vertex):
            dfs_f(v)

        group = [-1] * n_vertex
        x = 0

        def dfs_b(v: int) -> None:
            nonlocal x, group, gb

            if group[v] >= 0:
                return
            group[v] = x
            for nv in gb[v]:
                dfs_b(nv)
        for i in reversed(indexes):
            dfs_b(i)
            x += 1

        components: defaultdict[int, list[int]] = defaultdict(list)
        for i, g in enumerate(group):
            components[g].append(i)

        return [tuple(c) for _, c in components.items()]


class LIS(object):
    """ 最長増加部分列 (LIS; Longest Increasing Subsequence)
    """
    from collections.abc import Sequence

    def __init__(self) -> None:
        pass

    def lis(self, xs: Sequence[int]) -> int:
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


def divisors(n: int) -> list[int]:
    """ 約数列挙
    """
    assert n >= 0

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


class Tree(object):
    """ AVL木
    """

    def __init__(self) -> None:
        self.children = [None, None]


class MultiSet(object):
    from typing import Any

    def __init__(self) -> None:
        pass

    def add(self, x: Any) -> None:
        pass

    def lower_bound(self, x: Any) -> None:
        pass

    def upper_bound(self, x: Any) -> None:
        pass

    def has(self, x: Any) -> bool:
        return False


def cumsum(arr: list[int]) -> list[int]:
    """
    累積和
    """
    n = len(arr)
    cs = [0] * n
    for i in range(n):
        cs[i] = arr[i] + (cs[i - 1] if i > 0 else 0)
    return cs


def next_permutation(arr: list) -> list:
    n = len(arr)
    if n <= 1:
        return arr

    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            break
    for j in range(n - 1, -1, -1):
        if arr[j] > arr[i]:
            break
    arr[i], arr[j] = arr[j], arr[i]

    if i == 0 and j == 0:
        i = 0
        j = n - 1
    else:
        i = i + 1
        j = n - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return arr


def prev_permutation(arr: list) -> list:
    n = len(arr)
    if n <= 1:
        return arr

    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            break
    for j in range(n - 1, -1, -1):
        if arr[j] < arr[i]:
            break
    arr[i], arr[j] = arr[j], arr[i]

    if i == 0 and j == 0:
        i = 0
        j = n - 1
    else:
        i = i + 1
        j = n - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return arr


def kadane(arr: list[int]) -> int:
    """ Kadane's algorithm
        最大部分列問題(部分列の和の最大を求める)をO(n)で解く
    """
    import sys

    if not arr:
        return 0

    r = -sys.maxsize
    s = 0
    for a in arr:
        s = max(s + a, a)
        r = max(r, s)
    return r


import typing
from collections.abc import Sequence


def lcs(s: Sequence[typing.Any], t: Sequence[typing.Any]) -> int:
    """最長部分共通列 (longest common sequence)
    """
    ns = len(s)
    nt = len(t)
    assert ns == nt

    dp = [[0] * (nt + 1) for _ in range(ns + 1)]
    for i in range(ns):
        for j in range(nt):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = max(
                    dp[i + 1][j],
                    dp[i][j + 1],
                    dp[i][j] + 1
                )
            dp[i + 1][j + 1] = max(
                dp[i + 1][j + 1],
                dp[i + 1][j],
                dp[i][j + 1]
            )
    return dp[ns][nt]


def topological_sort_dfs(
    g: dict[int, list[int]],
    n: int,
) -> tuple[int, ...]:
    """トポロジカルソート (dfs版)
        g: グラフ
        n: ノードの数
        戻り値:
            トポロジカルソートした頂点の集合
            閉路を検出した場合はNone
        (Python 3.9以降はgraphlib.TopologicalSorterを使うべき)
    """
    ans = []
    visited = [0] * n

    def dfs(v: int) -> bool:
        visited[v] = 1
        for nv in g.get(v, []):
            if visited[nv] == 0:
                if not dfs(nv):
                    return False
            elif visited[nv] == 1:
                return False
        ans.append(v)
        visited[v] = 2
        return True

    for v in range(n):
        if visited[v] == 0:
            if not dfs(v):
                return ()

    return tuple(reversed(ans))


def topological_sort_bfs(
    g: dict[int, list[int]],
    n: int,
) -> tuple[int, ...]:
    """トポロジカルソート (bfs版)
        g: グラフ
        n: ノードの数
        戻り値:
            トポロジカルソートした頂点の集合
            閉路を検出した場合はNone
        (Python 3.9以降はgraphlib.TopologicalSorterを使うべき)
    """
    from collections import deque

    cnt = [0] * n
    for _, v in g.items():
        for x in v:
            cnt[x] += 1

    q = deque[int]()
    for i, c in enumerate(cnt):
        if c == 0:
            q.append(i)

    ans = []
    while q:
        x = q.pop()
        ans.append(x)
        n -= 1
        for y in g.get(x, []):
            if cnt[y] > 0:
                cnt[y] -= 1
                if cnt[y] == 0:
                    q.append(y)

    if n == 0:
        return tuple(ans)
    else:
        return ()


def topological_sort_unique(g: dict[int, list[int]], arr: list) -> bool:
    """トポロジカルソートの結果が一意かどうか
    """
    for i in range(1, len(arr)):
        if arr[i] not in g.get(arr[i - 1], []):
            return False
    return True


def crt(r: int, m: int) -> int:
    """ 中国剰余定理
    """
    return 0


def edit_distance(s: str, t: str) -> int:
    """ 編集距離 (レーベンシュタイン距離)
    """
    ns = len(s)
    nt = len(t)

    if ns == 0:
        return nt
    elif nt == 0:
        return ns

    dp = [[0] * (nt + 1) for _ in range(ns + 1)]
    for i in range(ns + 1):
        dp[i][0] = i
    for j in range(nt + 1):
        dp[0][j] = j

    for i in range(1, ns + 1):
        for j in range(1, nt + 1):
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + int(s[i - 1] != t[j - 1]),
            )

    return dp[ns][nt]


def multidim(*x):
    """多次元配列 (NumPy)
    """
    import numpy as np
    return np.zeros(x, dtype=np.int64)


def bisect_boundary(arr: list, f) -> int:
    """ [False, True]の境界の位置を検索する
    """
    assert callable(f)

    left = 0
    right = len(arr)
    while right - left > 1:
        mid = (left + right) // 2
        if f(arr[mid]):
            left = mid
        else:
            right = mid
    return left


# パスカルの三角形の計算
# Grundy数
# multiset, ordered set, 標準的な物があるなら
# AVL木
# 遅延セグメント木
# 用途を限定したMultiSet (heapで代用できる物など)
# trie
# メモリ使用量を抑える素因数分解
# 区間操作
# hash value

if __name__ == '__main__':
    pass
