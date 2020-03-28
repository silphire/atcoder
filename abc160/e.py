x, y, a, b, c = map(int, input().split())
pp = list(sorted(map(int, input().split()), reverse=True))[:x]
qq = list(sorted(map(int, input().split()), reverse=True))[:y]
rr = list(map(int, input().split()))

xx = list(sorted(pp + qq + rr, reverse=True))[:x+y]
print(sum(xx))
