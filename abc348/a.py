n = int(input())
s = ''
for i in range(n):
    if (i + 1) % 3 == 0:
        s += 'x'
    else:
        s += 'o'
print(s)