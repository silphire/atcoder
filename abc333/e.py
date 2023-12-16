from collections import defaultdict

n = int(input())
tt = [0] * n
xx = [0] * n
for i in range(n):
    t, x = map(int, input().split())
    tt[i] = t
    xx[i] = x

k = 0
kmin = 0
need = defaultdict(int)
pick = []
for i in range(n - 1, -1, -1):
    t = tt[i]
    x = xx[i]
    if t == 1:
        if need[x] > 0:
            pick.append(1)
            need[x] -= 1
            k -= 1
        else:
            pick.append(0)
    else:
        need[x] += 1
        k += 1
        kmin = max(kmin, k)

if max(need.values()) > 0:
    print(-1)
    exit()
print(kmin)
print(*reversed(pick))