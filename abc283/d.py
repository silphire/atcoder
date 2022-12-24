s = input()
n = len(s)

lp = [0] * n
box = {}
depth = 0
for i, c in enumerate(s):
    if c == '(':
        lp[depth] = i
        depth += 1
    elif c == ')':
        j = lp[depth]
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c in box and j <= box[c] <= i:
                del box[c]
        depth -= 1
    else:
        if c in box:
            print('No')
            exit()
        box[c] = i
print('Yes')