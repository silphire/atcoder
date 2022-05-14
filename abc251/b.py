n, w = map(int, input().split())
aa = list(map(int, input().split()))
ans = set()
for i in range(n):
    ans.add(aa[i])
    for j in range(i + 1, n):
        ans.add(aa[i] + aa[j])
        for k in range(j + 1, n):
            ans.add(aa[i] + aa[j] + aa[k])
print(len([a for a in ans if a <= w]))