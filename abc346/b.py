w, b = map(int, input().split())
s = 'wbwbwwbwbwbw'
ns = len(s)

for i in range(12):
    nw = 0
    nb = 0
    for j in range(w + b):
        if s[(i + j) % ns] == 'w':
            nw += 1
        else:
            nb += 1
    if nw == w and nb == b:
        print('Yes')
        exit()
print('No')