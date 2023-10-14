n, t = input().split()
n = int(n)
nt = len(t)
ans = []
for i in range(n):
    s = input()
    ns = len(s)
    if abs(ns - nt) > 1:
        continue
    d = 0
    j = 0
    k = 0
    while j < ns and k < nt:
        if s[j] == t[k]:
            j += 1
            k += 1
        else:
            d += 1
            if ns < nt:
                k += 1
            elif ns > nt:
                j += 1
            else:
                j += 1
                k += 1
        if d > 1:
            break
    if d <= 1:
        ans.append(i + 1)

print(len(ans))
print(*ans)