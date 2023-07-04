from collections import Counter

n = int(input())
aa = [
    int(input())
    for _ in range(n)
]

ans = 0
ctr = Counter(aa)
for k, v in ctr.items():
    ans += v * (v - 1) // 2
print(ans)