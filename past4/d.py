n = int(input())
s = list(input().rstrip())

xl = 0
xr = 0

while True:
    x = 0
    y = 0
    for i in range(n):
        if i > 0     and s[i] == '#' and s[i - 1] == '.':
            x += 1
        if i < n - 1 and s[i] == '#' and s[i + 1] == '.':
            y += 1
    if x == 0 and y == 0:
        break
    elif x >= y:
        xl += 1
        for i in range(1, n):
            if s[i] == '#' and s[i - 1] == '.':
                s[i - 1] = '#'
    else:
        xr += 1
        for i in range(n - 2, -1, -1):
            if s[i] =='#' and s[i + 1] == '.':
                s[i + 1] = '#'

print(f'{xl} {xr}')