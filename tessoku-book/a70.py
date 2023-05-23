from collections import deque

n, m = map(int, input().split())
aa = list(map(int, input().split()))
xyz = [
    list(map(lambda x: int(x) - 1, input().split()))
    for _ in range(m)
]

an = 0
for i, a in enumerate(aa):
    an |= a << i

dp = [-1] * (1 << n)
dp[an] = 0
q = deque([an])
while q:
    a = q.popleft()
    for x, y, z in xyz:
        b = a
        b ^= 1 << x
        b ^= 1 << y
        b ^= 1 << z
        if dp[b] == -1:
            dp[b] = dp[a] + 1
            q.append(b)

print(dp[-1])
