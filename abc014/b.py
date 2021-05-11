n, x = map(int, input().split())
aa = list(map(int, input().split()))

ans = 0
i = 0
while x > 0:
    if x & 1 == 1:
        ans += aa[i]
    i += 1
    x >>= 1
print(ans)