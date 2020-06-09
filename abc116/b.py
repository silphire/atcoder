s = int(input())

n = 2
ss = set([s])
while True:
    if s % 2 == 0:
        s //= 2
    else:
        s = 3 * s + 1
    if s in ss:
        break
    ss.add(s)
    n += 1
print(n)
