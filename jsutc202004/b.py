n = int(input())
bb = []
col = {'R': 0, 'B': 1}
for _ in range(n):
    x, c = input().rstrip().split()
    bb.append((col[c], int(x)))
bb = sorted(bb)
for b in bb:
    print(b[1])