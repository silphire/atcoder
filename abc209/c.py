import bisect

n = int(input())
cc = list(sorted(map(int, input().split())))
MOD = 10 ** 9 + 7
dd = []

ans = cc[0]
for i in range(1, n):
    ans *= max(0, cc[i] - i)
    ans %= MOD
print(ans)