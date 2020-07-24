n = int(input())
aa = tuple(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        ans = max(ans, abs(aa[i] - aa[j]))
print(ans)
