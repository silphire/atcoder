n = int(input())
hh = list(map(int, input().split()))

mh = 0
mi = 0
for i, h in enumerate(hh):
    if mh < h:
        mi = i
        mh = h
print(mi + 1)