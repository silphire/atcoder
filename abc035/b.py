s = input().rstrip()
t = int(input())

x = 0
y = 0
q = 0
for c in s:
    if c == '?':
        q += 1
    elif c == 'L':
        x -= 1
    elif c == 'R':
        x += 1
    elif c == 'U':
        y -= 1
    elif c == 'D':
        y += 1
d = abs(x) + abs(y)
if t == 1:
    print(d + q)
else:
    if d < q:
        print((q - d) % 2)
    else:
        print(d - q)