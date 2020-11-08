n = int(input())
aa = list(map(int, input().split()))

ans = 1
na = 0
for k in range(2, 10001):
    x = 0
    for a in aa:
        if a % k == 0:
            x += 1
    if x > na:
        ans = k
        na = x
print(ans)
