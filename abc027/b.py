n = int(input())
a = list(map(int, input().split()))
t = sum(a)
if t % n != 0:
    print(-1)
    exit()
t //= n

ans = 0
x = 0
b = 0

for i in range(n):
    x += a[i]
    if x % (b + 1) == 0 and x // (b + 1) == t:
        ans += b
        x = 0
        b = 0
    else:
        b += 1
print(ans)