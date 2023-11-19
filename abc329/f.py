n, q = map(int, input().split())
cc = list(map(int, input().split()))
cc = [{c} for c in cc]
for _ in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if len(cc[b]) >= len(cc[a]):
        cc[b] |= cc[a]
        cc[a].clear()
    else:
        cc[a] |= cc[b]
        cc[b].clear()
        cc[a], cc[b] = cc[b], cc[a]
    print(len(cc[b]))
