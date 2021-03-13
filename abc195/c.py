n = int(input())
ans = 0
f = 1000
while n >= f:
    ans += n - f + 1
    f *= 1000
print(ans)