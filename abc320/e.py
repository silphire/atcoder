import heapq

n, m = map(int, input().split())
qt = []
qm = [i for i in range(n)]
heapq.heapify(qm)
inq = [True] * n
ans = [0] * n
for _ in range(m):
    t, w, s = map(int, input().split())
    heapq.heappush(qt, (t, 1, w, s))

while qt:
    xs = heapq.heappop(qt)
    t = xs[0]

    if xs[1] == 0:
        # 列に戻る
        inq[xs[2]] = True
        heapq.heappush(qm, xs[2])
    elif qm:
        # 先頭の人が食べる
        m = heapq.heappop(qm)
        ans[m] += xs[2]
        inq[m] = False
        heapq.heappush(qt, (t + xs[3], 0, m))

for a in ans:
    print(a)