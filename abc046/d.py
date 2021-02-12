s = input().rstrip()

win = 0
lose = 0

for i, c in enumerate(s):
    if i % 2 == 0:
        m = 'g'
    else:
        m = 'p'
    
    if c == 'g' and m == 'p':
        win += 1
    elif c == 'p' and m == 'g':
        lose += 1

print(win - lose)
