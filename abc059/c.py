n = int(input())
aa = list(map(int, input().split()))

ans = float('inf')
for i in range(2):
    x = 0
    s = 0
    t = (-1) ** i
    for a in aa:
        if s + a == 0:
            x += 1
            if t > 0:
                s = 1
            else:
                s = -1
        elif s + a > 0:
            if t > 0:
                s += a
            else:
                x += s + a + 1
                s = -1
        else:
            if t > 0:
                x += abs(s + a) + 1
                s = 1
            else:
                s += a
        t *= -1
    ans = min(ans, x)
print(ans)
