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
            self.route[v1].append((w, v2))

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
                return w

            for wn, vn in self.route[v]:
                if goal is None:
                    distance[vn] = min(distance[vn], (w + wn))
                heapq.heappush(q, (w + wn, vn))

        if goal is None:
            return distance
        else:
            return float('inf')


n, m = map(int, input().split())
e1 = [None] * m
e2 = [None] * m
for i in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    e1[i] = (w, u, v)
    e2[i] = (w, v, u)

dj1 = Dijkstra(e1, n)
d1 = dj1.dijkstra(0)
dj2 = Dijkstra(e2, n)
d2 = dj2.dijkstra(n - 1)
for i in range(n):
    a = d1[i] + d2[i]
    if a == float('inf'):
        print(-1)
    else:
        print(a)