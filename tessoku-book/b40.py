from collections import Counter
n = int(input())
ctr = Counter(map(lambda x: int(x) % 100, input().split()))
ans = 0
for k, v in ctr.items():
    if k == 0 or k == 50:
        ans += v * (v - 1)
    else:
        ans += v * ctr[100 - k]
print(ans // 2)