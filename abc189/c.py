n = int(input())
aa = list(map(int, input().split()))

ans = 0
for l in range(n):
    a = aa[l]
    for r in range(l, n):
        a = min(a, aa[r])
        ans = max(ans, a * (r - l + 1))
print(ans)