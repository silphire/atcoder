a, b, c, k = map(int, input().split())
s, t = map(int, input().split())
x = a * s + b * t
if s + t >= k:
    x -= (s + t) * c
print(x)