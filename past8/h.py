import sys
sys.setrecursionlimit(3010)

class LCA(object):
    """
    Lowest Common Ancestor
    """
    def __init__(self, size):
        """ 保存領域の初期化。
            辺に重みがついている時の頂点間の重み計算にはcostを使えます。
        """
        self.size = size
        self.graph = [[] for _ in range(size)]
        self.cost_edge = [[] for _ in range(size)]

    def add_edge(self, x: int, y: int, cost: int = 1):
        """ 木の辺を追加します。
        """
        assert x < self.size
        assert y < self.size

        self.graph[x].append(y)
        self.graph[y].append(x)
        self.cost_edge[x].append(cost)
        self.cost_edge[y].append(cost)
    
    def init(self):
        """ 全ての辺を追加した後に、LCAを求める為の初期化をする。
        """
        s2 = 1
        while (1 << s2) < self.size:
            s2 += 1
        self.parent = [[-1] * s2 for _ in range(len(self.graph))]
        self.depth = [-1] * self.size
        self.cost_root = [0] * self.size

        def dfs(v, par, d, c):
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

    def lca(self, x: int, y: int):
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

    def dist(self, x: int, y: int):
        """ 2つの頂点間の距離を返します。
        """
        assert x < self.size
        assert y < self.size
        
        z = self.lca(x, y)
        return self.depth[x] + self.depth[y] - 2 * self.depth[z]
    
    def cost(self, x: int, y: int):
        """ 2つの頂点間のコストを返します。
        """
        assert x < self.size
        assert y < self.size
        
        z = self.lca(x, y)
        return self.cost_root[x] + self.cost_root[y] - 2 * self.cost_root[z]


n, x = map(int, input().split())
lca = LCA(n)
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    lca.add_edge(a - 1, b - 1, c)
lca.init()
for a in range(n):
    for b in range(a + 1, n):
        if lca.cost(a, b) == x:
            print('Yes')
            exit()
print('No')
