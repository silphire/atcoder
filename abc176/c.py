n = int(input())
aa = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    if aa[i - 1] > aa[i]:
        ans += aa[i - 1] - aa[i]
        aa[i] = aa[i - 1]
print(ans)