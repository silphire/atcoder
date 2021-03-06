n = int(input())
aa = []
bb = []
for i in range(n):
    a, b = map(int, input().split())
    aa.append((a, i))
    bb.append((b, i))
aa = sorted(aa)
bb = sorted(bb)
if aa[0][1] == bb[0][1]:
    print(min(aa[0][0] + bb[0][0], max(aa[0][0], bb[1][0]), max(aa[1][0], bb[0][0])))
else:
    print(max(aa[0][0], bb[0][0]))