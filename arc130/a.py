n = int(input())
s = input()

ans = 0
x = 0
p = ''
for c in s:
    if c == p:
        x += 1
    else:
        if x > 1:
            ans += x * (x - 1) // 2
        x = 1
        p = c
if x > 1:
    ans += x * (x - 1) // 2
print(ans)