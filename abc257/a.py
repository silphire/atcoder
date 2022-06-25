n, x = map(int, input().split())
p = ''
for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    p += c * n
print(p[x - 1])