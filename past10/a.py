a, b, c = map(int, input().split())
x = [a * b, b * c, c * a]
print(*[min(x), max(x)])