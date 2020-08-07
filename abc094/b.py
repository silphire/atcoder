n, m, x = map(int, input().split())
aa = tuple(map(int, input().split()))

c1 = 0
c2 = 0
for a in aa:
    if a < x:
        c1 += 1
    if a > x:
        c2 += 1
print(min(c1, c2))