n = int(input())
ss = [
    input()
    for _ in range(n)
]

m = max(len(s) for s in ss)

for i in range(m):
    t = ''
    for s in ss:
        if i < len(s):
            t = s[i] + t
        else:
            t = '*' + t
    while t[-1] == '*':
        t = t[:-1]
    print(t)