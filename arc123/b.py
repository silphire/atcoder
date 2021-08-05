n = int(input())
aa = list(sorted(map(int, input().split())))
bb = list(sorted(map(int, input().split())))
cc = list(sorted(map(int, input().split())))

ans = 0
i = 0
j = 0
k = 0
for i in range(n):
    while j < n and aa[i] >= bb[j]:
        j += 1
    if j == n:
        break
    while k < n and bb[j] >= cc[k]:
        k += 1
    if k == n:
        break
    j += 1
    k += 1
    ans += 1
print(ans)
