w, h = map(int, input().split())
pp = [(int(input()), 0) for _ in range(w)]
qq = [(int(input()), 1) for _ in range(h)]

edges = sorted(pp + qq)
w += 1
h += 1
ans = 0
for e, f in edges:
    if f == 0:
        ans += e * h
        w -= 1
    else:
        ans += e * w
        h -= 1
print(ans)