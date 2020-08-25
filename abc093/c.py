aa = list(sorted(map(int, input().split())))
nn = sum(map(lambda x: x % 2, aa))
ans = 0
if nn == 1:
    ans += 1
    for i in range(3):
        if aa[i] % 2 == 0:
            aa[i] += 1
elif nn == 2:
    ans += 1
    for i in range(3):
        if aa[i] % 2 == 1:
            aa[i] += 1
ans += (aa[2] - aa[0]) // 2
ans += (aa[2] - aa[1]) // 2
print(ans)