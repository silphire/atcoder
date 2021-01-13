n = int(input())
s = input().rstrip()

x = 0
m = 0
for i in range(n):
    if s[i] == 'I':
        x += 1
    else:
        x -= 1
    m = max(m, x)
print(m)