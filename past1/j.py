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
            return distance
        else:
            return float('inf')


h, w = map(int, input().split())
aa = [
    list(map(int, input().split()))
    for _ in range(h)
]

n = w * h
edges = []
for y in range(h):
    for x in range(w):
        p = y * w + x
        if x - 1 >= 0:
            edges.append((aa[y][x], p - 1, p))
        if x + 1 < w:
            edges.append((aa[y][x], p + 1, p))
        if y - 1 >= 0:
            edges.append((aa[y][x], p - w, p))
        if y + 1 < h:
            edges.append((aa[y][x], p + w, p))

dj = Dijkstra(edges, n)
lb = dj.dijkstra(w * (h - 1))
rb = dj.dijkstra(w * h - 1)
rt = dj.dijkstra(w - 1)

ans = float('inf')
for y in range(h):
    for x in range(w):
        p = y * w + x
        ans = min(ans, lb[p] + rb[p] + rt[p] + aa[h - 1][0] + aa[h - 1][w - 1] + aa[0][w - 1] - 2 * aa[y][x])
print(ans)