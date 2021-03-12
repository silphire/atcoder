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


class Kruskal(object):
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
            for j in range(i, n + 1, i):
                primes[j] = False
        return [i for i in range(2, n + 1) if primes[i]]


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
    def __init__(self):
        pass

# 高速なnCrの計算 w/ MOD 10**9+7
# scipy.special.comb(n, r)
# パスカルの三角形の計算
# 累積和。左右を操作するやつとか。

if __name__ == '__main__':
    pass