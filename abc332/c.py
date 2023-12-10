n, m = map(int, input().split())
s = input()

a = 0
b = 0
ans = 0
for c in s:
    if c == '0':
        ans = max(ans, max(0, a - m) + b)
        a = 0
        b = 0
    elif c == '1':
        a += 1
    else:
        b += 1
ans = max(ans, max(0, a - m) + b)
print(ans)