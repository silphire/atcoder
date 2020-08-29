s = input().rstrip()
t = input().rstrip()

ans = len(t)
for i in range(len(s)):
    n = 0
    for j in range(len(t)):
        if i + j >= len(s):
            n = 0
            break
        if s[i + j] == t[j]:
            n += 1
    ans = min(ans, len(t) - n)
print(ans)
