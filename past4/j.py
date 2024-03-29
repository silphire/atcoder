class Dijkstra(object):
    """
    * edges: [(weight, vertex_1, vertex_2)]
    """

    def __init__(self, edges, uni_edges, n_vertex: int):
        from collections import defaultdict

        assert n_vertex > 0

        self.edges = edges
        self.n_vertex = n_vertex

        self.route = defaultdict(list)

        for e in edges:
            w, v1, v2 = e[:3]
            self.route[v1].append((w, v2))
            self.route[v2].append((w, v1))
        for e in uni_edges:
            w, v1, v2 = e[:3]
            self.route[v1].append((w, v2))

    def dijkstra(self, start: int, goal: int):
        import heapq

        assert start < self.n_vertex
        assert goal < self.n_vertex

        visited = [False] * self.n_vertex

        q = [(0, start)]
        while q:
            w, v = heapq.heappop(q)
            if visited[v]:
                continue
            visited[v] = True

            if v == goal:
                return w

            for wn, vn in self.route[v]:
                if not visited[vn]:
                    heapq.heappush(q, (w + wn, vn))

        return float('inf')


n, m = map(int, input().split())
xab, xac, xbc = map(int, input().split())
s = input().rstrip()
ds = {'A': 0, 'B': 1, 'C': 2}
edges = []
uni_edges = [
    (xab, n + 0, n + 3 + 1),
    (xac, n + 0, n + 3 + 2),
    (xbc, n + 1, n + 3 + 2),
    (xab, n + 3 + 0, n + 1),
    (xac, n + 3 + 0, n + 2),
    (xbc, n + 3 + 1, n + 2),
]
for i in range(n):
    uni_edges.append((0, i, n + 0 + ds[s[i]]))
    uni_edges.append((0, n + 3 + ds[s[i]], i))

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((c, a, b))

dj = Dijkstra(edges, uni_edges, n + 3 * 2)
dist = dj.dijkstra(0, n - 1)
print(dist)