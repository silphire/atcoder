n, p, q = map(int, input().split())
dd = list(map(int, input().split()))

for d in dd:
    p = min(p, d + q)
print(p)