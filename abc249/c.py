from collections import Counter

n, k = map(int, input().split())

ss = [
    input().rstrip()
    for _ in range(n)
]
ans = 0
for x in range(2 ** n):
    ctr = Counter()
    for i in range(n):
        if x & (1 << i) != 0:
            ctr.update(ss[i])
    a = 0
    for _, c in ctr.items():
        if c == k:
            a += 1
    ans = max(ans, a)
print(ans)
