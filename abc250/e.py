n = int(input())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

d = {}
x = 0
for a in aa + bb:
    if a not in d:
        d[a] = x
        x += 1

aa = [d[a] for a in aa]
bb = [d[b] for b in bb]
sa = {aa[0]}
sb = {bb[0]}
aa[0] = (aa[0], 1)
bb[0] = (bb[0], 1)
for i in range(1, n):
    sa.add(aa[i])
    sb.add(bb[i])
    aa[i] = (max(aa[i], aa[i - 1][0]), len(sa))
    bb[i] = (max(bb[i], bb[i - 1][0]), len(sb))

q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    if aa[x - 1] == bb[y - 1]:
        print('Yes')
    else:
        print('No')