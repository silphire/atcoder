n = int(input())
s = list(input().rstrip())
q = int(input())
f = False
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 2:
        f = 1 - f
    else:
        a -= 1
        b -= 1
        if f:
            if a < n:
                a += n
            else:
                a -= n
            if b < n:
                b += n
            else:
                b -= n
        s[a], s[b] = s[b], s[a]
if f:
    s = s[n:] + s[:n]
print(''.join(s))