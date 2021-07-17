n, k = map(int, input().split())
cc = list(map(int, input().split()))

ans = 0
x = 0
ctr = {}
for i in range(n):
    if cc[i] not in ctr:
        ctr[cc[i]] = 0
        x += 1
    ctr[cc[i]] += 1

    if i - k >= 0:
        if ctr[cc[i - k]] == 1:
            x -= 1
            del ctr[cc[i - k]]
        else:
            ctr[cc[i - k]] -= 1
    
    ans = max(ans, x)
print(ans)