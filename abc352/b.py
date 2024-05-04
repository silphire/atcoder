s = input()
t = input()

i = 0
j = 0
ans = []
while i < len(s) and j < len(t):
    if s[i] == t[j]:
        ans.append(j + 1)
        i += 1
    j += 1
print(*ans)