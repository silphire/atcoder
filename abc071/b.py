s = tuple(sorted(set(input().rstrip())))
for c in list('abcdefghijklmnopqrstuvwxyz'):
    if c in s:
        continue
    print(c)
    exit()
print('None')