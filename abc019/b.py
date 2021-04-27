s = input().rstrip()
t = ''
p = None
n = 0
for c in s:
    if c == p:
        n += 1
    else:
        if p is not None:
            t += p + str(n)
        p = c
        n = 1
t += p + str(n)
print(t)
