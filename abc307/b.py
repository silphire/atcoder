n = int(input())
ss = [
    input()
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        s = ss[i] + ss[j]
        ln = len(s)
        f = True
        for k in range(ln):
            if s[k] != s[ln - 1 - k]:
                f = False
                break
        if f:
            print('Yes')
            exit()
print('No')