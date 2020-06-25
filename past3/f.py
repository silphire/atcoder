n = int(input())
a = ['' for _ in range(n)]
for i in range(n):
    a[i] = set(input().rstrip())

ans = ''
for i in range(n // 2 + n % 2):
    s = a[i] & a[n - 1 - i]
    if s:
        ans += list(s)[0]
    else:
        print(-1)
        exit(0)
rev = ''.join(reversed(ans))
if n % 2 == 1:
    print(ans + rev[1:])
else:
    print(ans+ rev)