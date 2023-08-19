s = input()
t = ''
for c in s:
    if c not in 'aeiou':
        t += c
print(t)
