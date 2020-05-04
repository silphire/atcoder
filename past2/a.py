def conv(f):
    if f[0] == 'B':
        return -int(f[1]) + 1
    else:
        return int(f[0])

s, t = list(input().rstrip().split())
s = conv(s)
t = conv(t)

print(max(s, t) - min(s, t))