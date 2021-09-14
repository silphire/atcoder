MOD = 10 ** 9 + 7
n = int(input())
aa = list(map(int, input().split()))

ans = 0
for x in range(60):
    b0 = 0
    b1 = 0
    mask = 1 << x
    for a in aa:
        if a & mask == 0:
            b0 += 1
        else:
            b1 += 1
    ans += mask * b0 * b1
    ans %= MOD
print(ans)