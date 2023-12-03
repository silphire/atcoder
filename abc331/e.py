n, m, l = map(int, input().split())
aa = list(map(int, input().split()))
bb = sorted([(a, i) for i, a in enumerate(map(int, input().split()))], reverse=True)
cd = set()
for i in range(l):
    c, d = map(int, input().split())
    cd.add((c - 1, d - 1))

ans = 0
for i, a in enumerate(aa):
    for (b, j) in bb:
        if (i, j) not in cd:
            ans = max(ans, a + b)
            break
print(ans)