n, m = map(int, input().split())
aa = list(map(int, input().split()))

t = sum(aa) / (4 * m)
c = 0
for a in aa:
    if a >= t:
        c += 1
if c >= m:
    print("Yes")
else:
    print("No")