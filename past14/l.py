from collections import defaultdict

def topological_sort_bfs(g, n: int):
    """トポロジカルソート (bfs版)
        g: グラフ
        n: ノードの数
        戻り値:
            トポロジカルソートした頂点の集合
            閉路を検出した場合はNone
    """
    import heapq

    cnt = [0] * n
    for k, v in g.items():
        for x in v:
            cnt[x] += 1

    q = []
    for i, c in enumerate(cnt):
        if c == 0:
            heapq.heappush(q, i)

    ans = []
    while q:
        x = heapq.heappop(q)
        ans.append(x)
        n -= 1
        for y in g.get(x, []):
            if cnt[y] > 0:
                cnt[y] -= 1
                if cnt[y] == 0:
                    heapq.heappush(q, y)

    if n == 0:
        return ans
    else:
        return None


n, m = map(int, input().split())
g = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
ans = topological_sort_bfs(g, n)
print(*map(lambda x: x + 1, ans))