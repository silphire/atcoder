n = int(input())
aa = [
    int(input())
    for _ in range(n)
]
l = 0
r = 0
ans = 0
while l < n:
    r = l
    while r < n:
        if aa[r] == 0:
            ans += sum(aa[l:r]) // 2
            l = r + 1
            break
        else:
            r += 1
    if l < r:
        ans += sum(aa[l:r]) // 2
        l = r + 1
print(ans)