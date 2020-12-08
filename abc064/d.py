n = int(input())
s = input().rstrip()

minp = 0
maxp = 0
x = 0
for i in range(n):
    if s[i] == '(':
        x += 1
        maxp = max(maxp, x)
    else:
        x -= 1
        minp = min(minp, x)
if minp < 0:
    s = ('(' * -minp) + s
    x += -minp
if x > 0:
    s += ')' * x
print(s)