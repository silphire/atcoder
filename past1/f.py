s = input().rstrip()
ans = []
left = 0
for i in range(len(s)):
    if i <= left or str.islower(s[i]):
        continue
    ans.append(s[left:i+1])
    left = i + 1
ans.append(s[left:])
print(''.join(sorted(ans, key=str.lower)))
