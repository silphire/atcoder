n = int(input())
aa = tuple(sorted(map(int, input().split()), reverse=True))

ans = 0
for i in range(1, n):
    ans += aa[i // 2]
print(ans)