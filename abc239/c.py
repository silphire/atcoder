x1, y1, x2, y2 = map(int, input().split())

def dist2(xa, ya, xb, yb):
    return (xa - xb) ** 2 + (ya - yb) ** 2

if dist2(x1, y1, x2, y2) > 20:
    print('No')
    exit()

for y in range(min(y1, y2) - 5, max(y1, y2) + 6):
    for x in range(min(x1, x2) - 5, max(x1, x2) + 6):
        if dist2(x, y, x1, y1) == 5 and dist2(x, y, x2, y2) == 5:
            print('Yes')
            exit()
print('No')