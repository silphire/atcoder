import itertools

MOD = 10 ** 9 + 7
n, k = map(int, input().split())

def solve(a, b):
    c = (b + a) * (b - a + 1) // 2
    return c

ans = 0
x = n
while x >= k - 1:
    a = solve(0, x)
    b = solve(n - x, n)
    ans += b - a + 1
    ans = ans % MOD
    x -= 1
print(ans)
