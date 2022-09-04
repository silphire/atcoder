n, a, b = map(int, input().split())
min_sum = a * (n - 1) + b
max_sum = a + (n - 1) * b
print(max(0, max_sum - min_sum + 1))