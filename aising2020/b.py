n = int(input())
aa = tuple(map(int, input().split()))

ans = 0
for i, a in enumerate(aa):
    if (i + 1) % 2 == 1 and a % 2 == 1:
        ans += 1
print(ans)
