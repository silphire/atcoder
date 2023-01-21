n, p, q, r, s = map(int, input().split())
p -= 1
q -= 1
r -= 1
s -= 1
aa = list(map(int, input().split()))
bb = [0] * n
for i in range(n):
    if p <= i <= q:
        bb[i] = aa[i - p + r]
    elif r <= i <= s:
        bb[i] = aa[i - r + p]
    else:
        bb[i] = aa[i]
print(*bb)