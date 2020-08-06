a, b, x = map(int, input().split())
x -= a
print(['NO', 'YES'][int(0 <= x <= b)])
