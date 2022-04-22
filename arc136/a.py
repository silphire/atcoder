n = int(input())
s = input().rstrip()

t = ''
x = 0
for c in s:
    if c == 'A':
        x += 2
    elif c == 'B':
        x += 1
    else:
        if x % 2 == 0:
            t += 'A' * (x // 2)
        else:
            t += 'A' * ((x - 1) // 2)
            t += 'B'
        x = 0
        t += 'C'
if x % 2 == 0:
    t += 'A' * (x // 2)
else:
    t += 'A' * ((x - 1) // 2)
    t += 'B'

print(t)
