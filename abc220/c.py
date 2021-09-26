n = int(input())
aa = list(map(int, input().split()))
x = int(input())
asum = sum(aa)
ans = x // asum * n
y = asum * ans // n
for a in aa:
    y += a
    ans += 1
    if y > x:
        break
print(ans)