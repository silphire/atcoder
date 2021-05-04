m, d = map(int, input().split())
print(['NO', 'YES'][int(m % d == 0)])