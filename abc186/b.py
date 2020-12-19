h, w = map(int, input().split())
amin = 10000
asum = 0
for i in range(h):
    a = list(map(int, input().split()))
    asum += sum(a)
    amin = min(amin, *a)
print(asum - amin * h * w)