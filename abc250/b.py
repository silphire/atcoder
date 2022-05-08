n, a, b = map(int, input().split())

c = ['.', '#']
ans = ''
for i in range(n):
    x = ''
    for j in range(n):
        x += c[(i + j) % 2] * b
    x += "\n"
    for j in range(a):
        ans += x
print(ans)