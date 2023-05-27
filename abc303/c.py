n, m, h, k = map(int, input().split())
s = input()
item = set([
    tuple(map(int, input().split()))
    for _ in range(m)
])

x = y = 0
for c in s:
    if c == 'R':
        x += 1
    elif c == 'L':
        x -= 1
    elif c == 'U':
        y += 1
    else:
        y -= 1
    h -= 1
    if h < 0:
        print('No')
        exit()
    if h < k and (x, y) in item:
        h = k
        item.discard((x, y))
print('Yes')