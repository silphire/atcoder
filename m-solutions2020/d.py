from collections import defaultdict

n = int(input())
aa = tuple(map(int, input().split()))

x = {0: 1000}
for i in range(n):
    xx = defaultdict(int)
    for stock, money in x.items():
        xx[0] = max(xx[0], money + stock * aa[i])
        ns = money // aa[i]
        xx[stock + ns] = max(xx[stock + ns], money - ns * aa[i])
    x = xx
print(x[0])