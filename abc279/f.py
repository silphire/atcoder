class UnionFind(object):
    """
    Union-Find (Disjoint Set Union)
    """
    def __init__(self, n: int):
        assert n > 0
        
        self.parent = [x for x in range(n)]
        self.size = [1] * n

    def root(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def is_same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def unite(self, x:int, y: int) -> int:
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

n, q = map(int, input().split())
box = [i for i in range(n + 1)]  # box no -> uf root
rbox = {i:i for i in range(n + 1)}  # uf root -> box no
uf = UnionFind(n + q + 1)  # ball

k = n
for _ in range(q):
    op, *arg = map(int, input().split())
    if op == 1:
        x, y = arg
        if not box[y]:
            continue
        if box[x]:
            r = uf.unite(box[x], box[y])
            box[x] = r
        else:
            r = box[x] = box[y]
        box[y] = None
        rbox[r] = x
    elif op == 2:
        x = arg[0]
        k += 1
        if box[x]:
            r = uf.unite(box[x], k)
        else:
            r = uf.root(k)
        box[x] = r
        rbox[r] = x
    else:
        x = arg[0]
        print(rbox[uf.root(x)])