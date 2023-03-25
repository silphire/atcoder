from collections import Counter
n = int(input())
aa = list(map(int, input().split()))
ctr = Counter(aa)
ans = 0
for c, nc in ctr.items():
    ans += nc // 2
print(ans)