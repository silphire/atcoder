n = int(input())
aa = tuple(map(int, input().split()))

ans = 0
for i in range(n):
    a = aa[i]
    while a % 2 == 0:
        ans += 1
        a //= 2
print(ans)
