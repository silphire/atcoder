n = int(input())

zmax = -float('inf')
zmin = float('inf')
wmax = -float('inf')
wmin = float('inf')

for i in range(n):
    x, y = map(int, input().split())
    zmax = max(zmax, x + y)
    zmin = min(zmin, x + y)
    wmax = max(wmax, x - y)
    wmin = min(wmin, x - y)

print(max(zmax - zmin, wmax - wmin))