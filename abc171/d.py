from collections import Counter

n = int(input())
aa = tuple(map(int, input().split()))
actr = Counter(aa)
q = int(input())

ans = sum([a * n for a, n in actr.items()])
for i in range(q):
    b, c = map(int, input().split())
    n = actr[b]
    ans = ans - b * n + c * n
    actr[c] += n
    del actr[b]
    print(ans)

