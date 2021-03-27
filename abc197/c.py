n = int(input())
aa = list(map(int, input().split()))

ans = 2 ** 31 - 1
for i in range(2 ** n):
    y = 0
    x = 0
    for j in range(n):
        x |= aa[j]
        if (i >> j) & 1 == 0:
            y ^= x
            x = 0
    if x != 0:
        y ^= x
    ans = min(ans, y)
print(ans)