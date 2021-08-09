a, b = map(int, input().split())
ans = []
if a >= b:
    for i in range(a):
        ans.append(i + 1)
    for i in range(b - 1):
        ans.append(-i - 1)
    x = 0
    for i in range(b, a + 1):
        x += i
    ans.append(-x)
else:
    for i in range(b):
        ans.append(-i - 1)
    for i in range(a - 1):
        ans.append(i + 1)
    x = 0
    for i in range(a, b + 1):
        x += i
    ans.append(x)
print(' '.join(map(str, ans)))
