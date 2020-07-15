s = input().rstrip()
k = int(input())

c = '1'
for i in range(min(len(s), k)):
    if s[i] != '1':
        c = s[i]
        break
print(c)