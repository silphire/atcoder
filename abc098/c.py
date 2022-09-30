n = int(input())
s = input().rstrip()

ae = [0] * (n + 1)
aw = [0] * (n + 1)
for i in range(n):
    if s[i] == 'E':
        ae[i] = 1
    else:
        aw[i] = 1
for i in range(n):
    ae[i + 1] += ae[i]
    aw[i + 1] += aw[i]

ans = n + 1
for i in range(n):
    a = ae[n - 1] - ae[i]
    if i > 0:
        a += aw[i - 1]
    ans = min(ans, a)
print(ans)