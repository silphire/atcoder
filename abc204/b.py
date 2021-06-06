n = int(input())
aa = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += max(0, aa[i] - 10)
print(ans)