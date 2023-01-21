n, x = map(int, input().split())
aa = [0] * n
bb = [0] * n
for i in range(n):
    aa[i], bb[i] = map(int, input().split())

dp = [[False] * (x + 1) for _ in range(n + 1)]

dp[0][0] = True
for i in range(n):
    for j in range(x + 1):
        if dp[i][j]:
            for k in range(bb[i] + 1):
                if j + aa[i] * k > x:
                    break
                dp[i + 1][j + aa[i] * k] = True
if dp[n][x]:
    print('Yes')
else:
    print('No')