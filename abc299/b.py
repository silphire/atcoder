n, t = map(int, input().split())
cc = list(map(int, input().split()))
rr = list(map(int, input().split()))

if t in cc:
    mi = 0
    mr = 0
    for i in range(n):
        if cc[i] == t:
            if rr[i] > mr:
                mr = rr[i]
                mi = i
    print(mi + 1)
else:
    mi = 0
    mr = 0
    for i in range(n):
        if cc[i] == cc[0]:
            if rr[i] > mr:
                mr = rr[i]
                mi = i
    print(mi + 1)
