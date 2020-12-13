import math

n, m = map(int, input().split())
aa = list(sorted(map(int, input().split())))
if m == 0:
    print(1)
    exit()

ln = []
for i in range(m):
    if i == 0:
        x = aa[i] - 1
    else:
        x = aa[i] - aa[i - 1] - 1
    if x > 0:
        ln.append(x)
x = n - aa[-1]
if x > 0:
    ln.append(x)

if not ln:
    print(0)
    exit()

k = min(ln)
ans = 0
for a in ln:
    ans += a // k + int(a % k > 0)
print(ans)