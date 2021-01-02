n = int(input())
v = []
x = 0
for i in range(n):
    a, b = map(int, input().split())
    v.append(2 * a + b)
    x -= a

v = sorted(v, reverse=True)
ans = 0
for vv in v:
    x += vv
    ans += 1
    if x > 0:
        print(ans)
        exit()
print(n)