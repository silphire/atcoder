s = input()
n = int(input())

ans = 0
f = 1 << (len(s) - 1)
for i in range(len(s)):
    if s[i] == '1':
        ans += f
    f >>= 1

f = 1 << (len(s) - 1)
for i in range(len(s)):
    if s[i] == '?' and ans + f <= n:
        ans += f
    f >>= 1

if ans > n:
    print(-1)
else:
    print(ans)