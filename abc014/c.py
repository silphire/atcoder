n = int(input())
a = [0] * n
b = [0] * n
e = set()
for i in range(n):
    a[i], b[i] = map(int, input().split())
    e.add(a[i])
    e.add(b[i])
d = {}
e = sorted(e)
for i, x in enumerate(e):
    d[x] = i
for i in range(n):
    a[i] = d[a[i]]
    b[i] = d[b[i]]
m = len(e) + 1
s = [0] * m
for i in range(n):
    s[a[i]] += 1
    s[b[i] + 1] -= 1
for i in range(1, m):
    s[i] += s[i - 1]
print(max(s))