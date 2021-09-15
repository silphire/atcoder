n = int(input())
test = [None] * n
for i in range(n):
    a = int(input())
    t = [None] * a
    for j in range(a):
        t[j] = tuple(map(int, input().split()))
    test[i] = t

ans = 0
for x in range(2 ** n):
    a = 0
    f = True
    for i in range(n):
        m = x & (1 << i) != 0
        if not m:
            continue
        a += 1

        for t in test[i]:
            mm = x & (1 << (t[0] - 1)) != 0
            if mm and t[1] == 1 or (not mm) and t[1] == 0:
                continue
            else:
                f = False
                break
        if not f:
            break
    if f:
        ans = max(ans, a)
print(ans)