from collections import Counter
n = int(input())
aa = list(map(int, input().split()))

ctr = Counter(aa)
nn = 0
for k, v in ctr.items():
    if v > 1:
        nn += v - 1

aa = list(sorted(set(aa)))
n = len(aa)

x = 0
p = 0
while p < n:
    if aa[p] == x + 1:
        x += 1
        p += 1
    else:
        if nn >= 2:
            x += 1
            nn -= 2
        elif nn == 1 and p + 1 <= n:
            n -= 1
            nn = 0
            x += 1
        elif p + 2 <= n:
            n -= 2
            x += 1
        else:
            break

nn += n - p
while nn >= 2:
    x += 1
    nn -= 2

print(x)