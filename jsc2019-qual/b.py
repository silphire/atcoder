n, k = map(int, input().split())
aa = list(map(int, input().split()))
MOD = 10 ** 9 + 7

x = 0
for i in range(n):
    for j in range(i + 1, n):
        if aa[i] > aa[j]:
            x += 1
ans = x * k

x = 0
for i in range(n):
    for j in range(n):
        if aa[i] > aa[j]:
            x += 1
ans += x * k * (k - 1) // 2

ans %= MOD
print(ans)