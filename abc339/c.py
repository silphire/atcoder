n = int(input())
aa = list(map(int, input().split()))

mc = 0
c = 0
for a in aa:
    c += a
    mc = min(mc, c)
print(-mc + c)