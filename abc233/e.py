x = list(map(int, list(input().rstrip())))
n = len(x)
a = [0] * n
s = 0
for i in range(n):
    s += x[i]
    a[i] = s
r = 0
for i in range(n):
    a[n - 1 - i] += r
    r = a[n - 1 - i] // 10
    a[n - 1 - i] %= 10
if r > 0:
    a = [r] + a
print(''.join(list(map(str, a))))