n = int(input())
aa = list(map(int, input().split()))

ans = float('-inf')
x = 0
diff = 0
maxdiff = 0
for i in range(n):
    diff += aa[i]
    maxdiff = max(maxdiff, diff)
    ans = max(ans, x + maxdiff)
    x += diff
print(ans)