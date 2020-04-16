s = input().rstrip()
t = input().rstrip()
n = 0
for i in range(len(s)):
    if s[i] == t[i]:
        n += 1
print(n)
