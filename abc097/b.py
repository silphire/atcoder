import bisect

x = int(input())

s = {1}
for a in range(2, 1000):
    for b in range(2, 11):
        c = a ** b
        if c > 1000:
            break
        s.add(c)
s = sorted(s, reverse=True)
for a in s:
    if a <= x:
        print(a)
        exit(0)
