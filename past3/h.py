n, l = map(int, input().split())
x = set(map(int, input().split()))
t = tuple(map(int, input().split()))
INF = 10 ** 10

pp = [INF for _ in range(10 ** 5 + 10)]
pp[0] = 0
for i in range(l):
    d = pp[i]
    if i in x:
        d += t[2]
    
    pp[i + 1] = min(pp[i + 1], d + t[0])
    
    if i + 1 == l:
        pp[i + 1] = min(pp[i + 1], d + (t[0] + t[1]) // 2)
    pp[i + 2] = min(pp[i + 2], d + t[0] + t[1])

    if i + 2 == l:
        pp[i + 2] = min(pp[i + 2], d + (t[0] + t[1] * 3) // 2)
    if i + 3 == l:
        pp[i + 3] = min(pp[i + 3], d + (t[0] + t[1] * 5) // 2)
    pp[i + 4] = min(pp[i + 4], d + t[0] + t[1] * 3)

print(int(pp[l]))