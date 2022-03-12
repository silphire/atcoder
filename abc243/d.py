n, x = map(int, input().split())
s = input().rstrip()

d = 0
for c in s:
    if c == 'U':
        d -= 1
    else:
        d += 1

if d < 0:
    x //= 2 ** -d

cd = 0
for c in s:
    if c == 'U':
        cd -= 1
        if cd < d:
            x //= 2
    else:
        if cd < d:
            if c == 'L':
                x = x * 2
            else:
                x = x * 2 + 1
        cd += 1
print(x)