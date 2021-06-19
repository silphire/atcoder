from collections import Counter
n = int(input())
aa = list(map(int, input().split()))
ctr = Counter(aa)

ans = 0
for i, a in enumerate(aa):
    ans += n - i - ctr[a]
    ctr[a] -= 1
print(ans)