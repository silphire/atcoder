n = int(input())
aa = list(map(int, input().split()))
m = int(input())
bb = set(map(int, input().split()))
x = int(input())

dp = [False] * (3 * 10 ** 5)
dp[0] = True
for i in range(x):
    if not dp[i]:
        continue
    for a in aa:
        if (i + a) not in bb:
            dp[i + a] = True
if dp[x]:
    print('Yes')
else:
    print('No')