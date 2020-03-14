a, b, c = map(int, input().split())

d = c - a - b
cond = d > 0 and 4 * a * b < d ** 2
if cond:
    print("Yes")
else:
    print("No")