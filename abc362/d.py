class Dijkstra(object):
    """
    ダイクストラ法 -- 最短経路探索
    * edges: [(weight, vertex_1, vertex_2)]
    """

    from enum import IntEnum

    class Priority(IntEnum):
        MIN = 1
        MAX = -1

    def __init__(
            self,
            edges: list[tuple[int, int, int]],
            vertexes: list[int],
            n_vertex: int,
            bidirectional: bool = True,
            priority: Priority = Priority.MIN
    ):
        from collections import defaultdict

        assert n_vertex > 0

        self.edges = edges
        self.vertexes = vertexes
        self.n_vertex = n_vertex
        self.priority = priority

        self.route: dict[int, list[tuple[int, int]]] = defaultdict(list)

        for e in edges:
            w, v1, v2 = e[:3]
            assert w >= 0
            self.route[v1].append((self.priority * w, v2))
            if bidirectional:
                self.route[v2].append((self.priority * w, v1))

    def dijkstra(self, start: int, goal: int) -> int:
        """ startで示す頂点からgoalで示す頂点までの最短経路を求める
            start: 始点の頂点
            goal: 終点の頂点
            return: 始点から終点までの最短距離。到達できないなら-maxsize
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
            start: 始点
            return: 各頂点への最短距離。到達できない場合はmaxsize
        """
        import heapq
        import sys

        assert 0 <= start < self.n_vertex

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
                distance[vn] = min(distance[vn], self.priority * (w + wn + self.vertexes[vn]))
                heapq.heappush(q, (w + wn + self.vertexes[vn], vn))

        return distance


n, m = map(int, input().split())
aa = list(map(int, input().split()))
ee = []
for i in range(m):
    u, v, b = map(int, input().split())
    u -= 1
    v -= 1
    ee.append((b, u, v))


dj = Dijkstra(ee, aa, n)
ans = dj.dijkstra_all_dests(0)
print(*[a + aa[0] for a in ans[1:]])