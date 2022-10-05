s = input().rstrip()
ans = 0
x = 0
i = 0
while i < len(s):
    if s[i:i+2] == 'BC':
        ans += x
        i += 1
    elif s[i] == 'A':
        x += 1
    elif s[i] == 'B' or s[i] == 'C':
        x = 0
    i += 1
print(ans)