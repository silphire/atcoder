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
            w, t, v1, v2 = e[:4]
            self.route[v1].append((self.priority * w, t, v2))
            self.route[v2].append((self.priority * w, t, v1))

    def dijkstra(self, start: int, goal=None):
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

        q = [(0, 0, start)]
        while q:
            w, t, v = heapq.heappop(q)
            if visited[v]:
                continue
            visited[v] = True

            if goal is not None and v == goal:
                return (self.priority * w, t)

            for wn, tn, vn in self.route[v]:
                if goal is None:
                    distance[vn] = min(distance[vn], self.priority * (w + wn))
                heapq.heappush(q, (w + wn, t + tn, vn))

        return (float('inf'), 0)


n, m = map(int, input().split())
edges = [None] * m
for i in range(m):
    a, b, c, d = map(int, input().split())
    edges[i] = (c, -d, a, b)
dj = Dijkstra(edges, n + 1)
w, t = dj.dijkstra(1, n)
print(w, -t)