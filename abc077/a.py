c1 = tuple(input().rstrip())
c2 = tuple(reversed(input().rstrip()))
print(['NO', 'YES'][int(c1 == c2)])