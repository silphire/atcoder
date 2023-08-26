n, h, x = map(int, input().split())
pp = list(map(int, input().split()))

for i, p in enumerate(pp):
    if h + p >= x:
        print(i + 1)
        exit()