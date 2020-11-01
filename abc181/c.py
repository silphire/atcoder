import itertools

n = int(input())
ps = [tuple(map(int, input().split())) for _ in range(n)]

for a, b, c in itertools.combinations(ps, 3):
    x1 = b[0] - a[0]
    x2 = c[0] - b[0]
    y1 = b[1] - a[1]
    y2 = c[1] - b[1]
    if x1 * y2 == x2 * y1:
        print('Yes')
        exit()
print('No')