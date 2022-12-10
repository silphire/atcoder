n, t = map(int, input().split())
aa = list(map(int, input().split()))

t %= sum(aa)
for i, a in enumerate(aa):
    if t < a:
        print(i + 1, t)
        exit()
    t -= a