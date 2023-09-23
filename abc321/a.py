n = input()
p = None
for c in n:
    if p is None:
        p = int(c)
    else:
        x = int(c)
        if x >= p:
            print('No')
            exit()
        p = x
print('Yes')