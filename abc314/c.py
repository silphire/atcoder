n, m = map(int, input().split())
s = list(input())
t = [None] * n
cc = list(map(int, input().split()))
cr = [list() for _ in range(m)]
for i, c in enumerate(cc):
    cr[c - 1].append(i)

ct = []
for c in range(m):
    ct.append(cr[c][1:] + [cr[c][0]])

for c in range(m):
    for i in range(len(cr[c])):
        p = cr[c][i]
        q = ct[c][i]
        t[q] = s[p]
print(''.join(t))