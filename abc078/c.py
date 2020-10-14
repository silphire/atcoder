n, m = map(int, input().split())
ans = ((n - m) * 100 + m * 1900) * (2 ** m)
print(ans)