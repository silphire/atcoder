n = int(input())
a = tuple(map(int, input().split()))
total = sum(a)
target = total // 2

a = a + a
n *= 2

ans = float('inf')
x = 0
y = 0
cur = 0
while y < n:
    while y < n and cur < target:
        cur += a[y]
        y += 1
        ans = min(ans, abs(total - cur - cur))
    while x <= y and cur > target:
        cur -= a[x]
        x += 1
        ans = min(ans, abs(total - cur - cur))

    if abs(cur - target) <= 1:
        print(total - cur - cur)
        exit()
print(ans)