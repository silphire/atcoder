n = int(input())
aa = [0] * n
bb = [0] * n
for i in range(n):
    aa[i], bb[i] = map(int, input().split())

x = 0
for i in range(n - 1, -1, -1):
    r = (aa[i] + x) % bb[i]
    if r > 0:
        x += bb[i] - r
print(x)