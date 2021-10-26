n = int(input())
aa = list(map(int, input().split()))

ans = float('-inf')
for i in range(n):
    mst = float('-inf')
    msa = float('-inf')
    for j in range(n):
        if i == j:
            continue
        a = min(i, j)
        b = max(i, j)
        f = True
        st = 0
        sa = 0
        for x in range(a, b + 1):
            if f:
                st += aa[x]
            else:
                sa += aa[x]
            f = not f
        if msa < sa:
            msa = sa
            mst = st
    ans = max(ans, mst)
print(ans)