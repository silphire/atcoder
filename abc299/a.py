n = int(input())
s = input()
w = 0
for c in s:
    if c == '*':
        if w == 1:
            print('in')
            exit()
    elif c == '|':
        w += 1
print('out')