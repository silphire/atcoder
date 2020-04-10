n, k = map(int, input().split())
h = list(map(int, input().split()))

x = 0
for hh in h:
    if hh >= k:
        x += 1
print(x)