a, b, c = map(int, input().split())
ans  = a * (a + 1) // 2
ans *= b * (b + 1) // 2
ans *= c * (c + 1) // 2

print(ans % 998244353)
