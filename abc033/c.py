s = input().rstrip()
ans = 0
for e in s.split('+'):
    if '0' not in e:
        ans += 1
print(ans)