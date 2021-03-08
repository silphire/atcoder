n = int(input())
s = [
    input().rstrip()
    for _ in range(n)
]
t = [
    [''] * n
    for _ in range(n)
]

for y in range(n):
    for x in range(n):
        t[x][n - 1 - y] = s[y][x]

for i in range(n):
    print(''.join(t[i]))