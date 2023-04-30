n, k = map(int, input().split())
aa = [0] * n
bb = [0] * n
for i in range(n):
    aa[i], bb[i] = map(int, input().split())

ans = 0
for a in range(1, 101):
    for b in range(1, 101):
        x = 0
        for i in range(n):
            if 0 <= aa[i] - a <= k and 0 <= bb[i] - b <= k:
                x += 1
        ans = max(ans, x)
print(ans)