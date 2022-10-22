n = int(input())
aa = list(map(int, input().split()))
bb = [0] * (4 * n + 4)
for i, a in enumerate(aa):
    k = 2 * (i + 1)
    bb[k] = bb[a] + 1
    bb[k + 1] = bb[a] + 1
for b in bb[1:2*n+2]:
    print(b)
