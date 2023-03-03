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
            # self.route[v2].append((self.priority * w, v1))

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
            return float('inf')
        else:
            return distance

ee = []
n, m = map(int, input().split())
aa = list(map(int, input().split()))

for i in range(n):
    ee.append((aa[i], i, i + 1))
for i in range(m):
    b, l, r = map(int, input().split())
    ee.append((b, l - 1, r))
for i in range(n):
    ee.append((0, i + 1, i))

dj = Dijkstra(ee, n + 1, Dijkstra.MIN)
ans = dj.dijkstra(0, n)
print(ans)