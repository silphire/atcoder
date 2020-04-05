s, l, r = map(int, input().split())
if l <= s <= r:
    print(s)
else:
    if abs(s - l) < abs(s - r):
        print(l)
    else:
        print(r)
        