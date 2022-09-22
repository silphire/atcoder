n, k, s = map(int, input().split())
if s == 10 ** 9:
    a = ([s] * k) + ([s - 1] * (n - k))
else:
    a = ([s] * k) + ([s + 1] * (n - k))
print(*a)