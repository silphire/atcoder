n, k = map(int, input().split())
rr = sorted(map(int, input().split()))

c = 0
for i in range(n - k, n):
    c = (c + rr[i]) / 2
print(c)