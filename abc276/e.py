from collections import deque
import itertools

h, w = map(int, input().split())
cc = [
    list(input().rstrip())
    for _ in range(h)
]

sx = sy = None
for i in range(h):
    for j in range(w):
        if cc[i][j] == 'S':
            sx = j
            sy = i
            break
    if sx is not None:
        break

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

    def unite(self, x:int, y: int) -> None:
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return

        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx

        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
    
    def get_size(self, x: int) -> int:
        return self.size[self.root(x)]


uf = UnionFind(w * h)
q = deque()
cands = []
if sx - 1 >= 0 and cc[sy][sx - 1] == '.':
    q.append((sx - 1, sy))
    cands.append(sy * w + sx - 1)
if sx + 1 < w and cc[sy][sx + 1] == '.':
    q.append((sx + 1, sy))
    cands.append(sy * w + sx + 1)
if sy - 1 >= 0 and cc[sy - 1][sx] == '.':
    q.append((sx, sy - 1))
    cands.append((sy - 1) * w + sx)
if sy + 1 < h and cc[sy + 1][sx] == '.':
    q.append((sx, sy + 1))
    cands.append((sy + 1) * w + sx)

while q:
    x, y = q.popleft()
    if not (0 <= x < w and 0 <= y < h):
        continue
    if cc[y][x] == 'v':
        continue
    cc[y][x] = 'v'

    if y - 1 >= 0 and cc[y - 1][x] == '.':
        q.append((x, y - 1))
        uf.unite(y * w + x, (y - 1) * w + x)
    if y + 1 < h and cc[y + 1][x] == '.':
        q.append((x, y + 1))
        uf.unite(y * w + x, (y + 1) * w + x)
    if x - 1 >= 0 and cc[y][x - 1] == '.':
        q.append((x - 1, y))
        uf.unite(y * w + x, y * w + x - 1)
    if x + 1 < w and cc[y][x + 1] == '.':
        q.append((x + 1, y))
        uf.unite(y * w + x, y * w + x + 1)

for p, q in itertools.combinations(cands, 2):
    if uf.is_same(p, q):
        print('Yes')
        exit()
print('No')
