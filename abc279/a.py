s = input().rstrip()
a = 0
for c in s:
    if c == 'v':
        a += 1
    else:
        a += 2
print(a)