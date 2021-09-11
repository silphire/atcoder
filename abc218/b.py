pp = list(map(int, input().split()))
s = 'abcdefghijklmnopqrstuvwxyz'
ans = ''
for p in pp:
    ans += s[p - 1]
print(ans)