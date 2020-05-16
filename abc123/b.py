ans = 0
s = 100
for i in range(5):
    a = int(input())
    r = a % 10
    if r > 0:
        s = min(s, r)
    ans += a // 10 * 10 + (10 if r > 0 else 0)
if s == 100:
    print(ans)
else:
    print(ans + s - 10)
