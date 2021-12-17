n = int(input())
aa = list(map(lambda x: int(x) - 1, input().split()))

ans = 0
for i in range(n):
    j = aa[i]
    if aa[j] == i:
        ans += 1
print(ans // 2)