s = input().rstrip()

n = 0
for i in range(len(s) // 2):
    if s[i] != s[-i-1]:
        n += 1
print(n)