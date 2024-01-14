n = int(input())
x = 0
ans = 0
n -= 1
while n > 0:
    r = n % 5
    ans += 2 * r * (10 ** x)
    n //= 5
    x += 1
print(ans)