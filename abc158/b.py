n, a, b = map(int, input().split())
x = a + b
ans = n // x * a
ans += min(a, (n % x))
print(ans)