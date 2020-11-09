n, m = map(int, input().split())
s = [
    input().rstrip()
    for _ in range(n)
]
for y in range(n):
    aa = ''
    for x in range(m):
        a = 0
        for j in range(-1, 2):
            for i in range(-1, 2):
                xx = x + i
                yy = y + j
                if 0 <= xx < m and 0 <= yy < n and s[yy][xx] == '#':
                    a += 1
        aa += str(a)
    print(aa)
