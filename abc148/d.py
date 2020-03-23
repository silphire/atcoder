n = int(input())
aa = list(map(int, input().split()))

ans = 0
x = 1
for a in aa:
    if a == x:
        x += 1
    else:
        ans += 1
if x == 1:
    print(-1)
else:
    print(ans)