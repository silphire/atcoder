n = int(input())
aa = list(map(int, input().split()))
f = [False] * n

for i in range(n):
    if f[i]:
        continue
    ans = []
    sa = set()
    j = i
    while not f[j]:
        f[j] = True
        ans.append(j + 1)
        sa.add(j + 1)
        j = aa[j] - 1
    if (j + 1) in sa:
        k = ans.index(j + 1)
        print(len(ans) - k)
        print(*ans[k:])
        exit()