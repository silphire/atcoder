n = int(input())
aa = tuple(map(int, input().split()))

total = sum(aa)
x = aa[0]
ans = abs(x - (total - x))
for i in range(1, n - 1):
    x += aa[i]
    ans = min(ans, abs(x - (total - x)))
print(ans)