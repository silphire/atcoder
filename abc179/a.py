s = input().rstrip()

if s[-1] == 's':
    s += 'es'
else:
    s += 's'
print(s)