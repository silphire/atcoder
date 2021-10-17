s = input().rstrip()
a = set()
for i in range(len(s)):
    x = s[i:] + s[:i]
    a.add(x)
a = sorted(a)
print(a[0])
print(a[-1])