n, d = map(int, input().split())
ss = [
    input()
    for _ in range(n)
]

ans = 0
a = 0
for i in range(d):
    f = True
    for j in range(n):
        if ss[j][i] == 'x':
            f = False
            a = 0
            break
    if f:
        a += 1
    ans = max(ans, a)
print(ans)