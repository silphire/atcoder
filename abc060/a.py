a, b, c = input().rstrip().split()
print(['NO', 'YES'][int(a[-1] == b[0] and b[-1] == c[0])])
