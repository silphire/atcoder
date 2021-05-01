s = input().rstrip()
ans = 0
for i in range(len(s)):
    if s[i:i+4] == 'ZONe':
        ans += 1
print(ans)
