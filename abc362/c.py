n = int(input())
ll = [0] * n
rr = [0] * n
for i in range(n):
    ll[i], rr[i] = map(int, input().split())

sl = sum(ll)
sr = sum(rr)
if sl <= 0 and sr >= 0:
    print('Yes')
    rem = sr
    for i in range(n):
        if rr[i] - rem < ll[i]:
            rem -= rr[i] - ll[i]
            rr[i] = ll[i]
        else:
            rr[i] -= rem
            rem = 0
            break
    print(*rr)
else:
    print('No')