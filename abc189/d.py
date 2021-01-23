n = int(input())

f = 1
t = 1
for i in range(n):
    s = input().rstrip()
    if s == 'AND':
        nt = t
        nf = t + 2 ** (i + 1)
    else:
        nt = t + 2 ** (i + 1)
        nf = f
    t = nt
    f = nf
print(t)