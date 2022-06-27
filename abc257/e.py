n = int(input())
cc = [float('inf')] + list(map(int, input().split()))

mc = min(cc)
anslen = n // mc

co = sorted([(-i, cc[i]) for i in range(9, 0, -1)])
for i in range(9, 0, -1):
    if cc[i] == mc:
        md = i
        break

ans = ''
need = mc * anslen
for i in range(anslen):
    if n == need:
        ans += str(md) * (anslen - i)
        break
    need -= mc
    for d in range(9, 0, -1):
        if n - cc[d] >= need:
            ans += str(d)
            n -= cc[d]
            break
print(ans)