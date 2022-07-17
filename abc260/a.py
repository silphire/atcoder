s = sorted(list(input().rstrip()))
if len(set(s)) == 1:
    print(-1)
elif s[0] == s[1]:
    print(s[2])
else:
    print(s[0])