n, q = map(int, input().split())
ss = []
for _ in range(q):
    ss.append(list(map(lambda x: int(x) - 1, input().split())))

ans = [[False for _ in range(n)] for _ in range(n)]
for log in ss:
    if log[0] == 0:
        # follow
        ans[log[1]][log[2]] = True
    elif log[0] == 1:
        # follow back them all
        for i in range(n):
            if i == log[1]:
                continue
            if ans[i][log[1]]:
                ans[log[1]][i] = True
    else:
        adds = set()
        for i in range(n):
            if ans[log[1]][i]:
                for j in range(n):
                    if ans[i][j] and log[1] != j:
                        adds.add(j)
        for x in adds:
            ans[log[1]][x] = True

for a in ans:
    print(''.join(['Y' if f else 'N' for f in a]))
