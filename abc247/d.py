q = int(input())
que = []
p = None
for _ in range(q):
    x = tuple(map(int, input().split()))
    if x[0] == 1:
        que.append(x[1:])
        if p is None:
            p = 0
    else:
        ans = 0
        c = x[1]
        while c > 0:
            if que[p][1] > c:
                ans += que[p][0] * c
                que[p] = (que[p][0], que[p][1] - c)
                c = 0
            else:
                ans += que[p][0] * que[p][1]
                c -= que[p][1]
                p += 1
        print(ans)