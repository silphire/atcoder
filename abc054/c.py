from collections import defaultdict
import sys

sys.setrecursionlimit(10000)

n, m = map(int, input().split())
g = defaultdict(set)
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].add(b)
    g[b].add(a)

visited = [False] * n

def visit(node, remain):
    global visited
    global g

    if visited[node]:
        return 0
    if remain == 1:
        return 1

    visited[node] = True
    ans = 0
    for next_node in g[node]:
        ans += visit(next_node, remain - 1)
    visited[node] = False

    return ans

print(visit(0, n))
