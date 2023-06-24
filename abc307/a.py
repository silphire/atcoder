n = int(input())
aa = list(map(int, input().split()))

ans = [0] * n
for i in range(n):
    for j in range(7):
        ans[i] += aa[i * 7 + j]
print(*ans)