from collections import defaultdict
import sys

N = 10 ** 5 + 1
sys.setrecursionlimit(N)

tree = defaultdict(list)
visited = [False] * N
distance = [0] * N

n = int(input())
for i in range(1, n):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

def f(x, d):
    global tree
    global visited

    distance[x] = d
    visited[x] = True
    for nx, nd in tree[x]:
        if not visited[nx]:
            f(nx, d + nd)
    visited[x] = False

q, k = map(int, input().split())
f(k, 0)

for i in range(q):
    x, y = map(int, input().split())
    print(distance[x] + distance[y])