n, m = map(int, input().split())
hh = list(map(int, input().split()))

for i, h in enumerate(hh):
    if m < h:
        print(i)
        exit()
    else:
        m -= h
print(n)