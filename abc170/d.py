from collections import Counter

n = int(input())
aa = tuple(sorted(map(int, input().split())))
cnt = Counter(aa)
amax = max(aa)
af = [False] * (amax + 1)

ans = 0
for i in range(n):
    x = aa[i]
    if af[x]:
        continue
    while x <= amax:
        af[x] = True
        x += aa[i]
    if cnt[aa[i]] == 1:
        ans += 1

print(ans)