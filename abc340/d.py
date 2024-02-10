class Dijkstra(object):
    """
    * edges: [(weight, vertex_1, vertex_2)]
    """

    from enum import IntEnum

    class Priority(IntEnum):
        MIN = 1
        MAX = -1

    def __init__(
            self,
            edges: list[tuple[int, int, int]],
            n_vertex: int,
            priority: Priority = Priority.MIN
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
            # self.route[v2].append((self.priority * w, v1))

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


n = int(input())
edges = []
for i in range(1, n):
    a, b, x = map(int, input().split())
    edges.append((a, i, i + 1))
    edges.append((b, i, x))

dj = Dijkstra(edges, n + 1)
ans = dj.dijkstra(1, n)
print(ans)