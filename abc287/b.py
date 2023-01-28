n, m = map(int, input().split())
ss = [input() for _ in range(n)]
tt = set([input() for _ in range(m)])
x = 0
for s in ss:
    if s[3:] in tt:
        x += 1
print(x)