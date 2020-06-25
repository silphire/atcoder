n = int(input())
s = input()
x = 0
for i in range(len(s)):
    if s[i:i+3] == 'ABC':
        x += 1
print(x)
