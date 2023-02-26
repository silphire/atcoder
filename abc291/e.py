def topological_sort_bfs(g, n: int):
    """トポロジカルソート (bfs版)
        g: グラフ
        n: ノードの数
        戻り値: 
            トポロジカルソートした頂点の集合
            閉路を検出した場合はNone
    """
    from collections import deque

    cnt = [0] * n
    for k, v in g.items():
        for x in v:
            cnt[x] += 1

    q = deque()
    for i, c in enumerate(cnt):
        if c == 0:
            q.append(i)

    ans = []
    while q:
        x = q.pop()
        ans.append(x)
        n -= 1
        for y in g.get(x, []):
            if cnt[y] > 0:
                cnt[y] -= 1
                if cnt[y] == 0:
                    q.append(y)

    if n == 0:
        return ans
    else:
        return None

    
from collections import defaultdict

g = defaultdict(list)
n, m = map(int, input().split())
for _ in range(m):
    x, y = map(int, input().split())
    g[x - 1].append(y - 1)
r = topological_sort_bfs(g, n)
for i in range(1, n):
    if r[i] not in g[r[i - 1]]:
        print('No')
        exit()

print('Yes')
ans = [0] * n
for i in range(n):
    ans[r[i]] = i + 1
print(*ans)