s = input().rstrip()
t = input().rstrip()
n = len(s)
for c, d in zip(list(s), list(t)):
    if not (c == d or c == '@' and d in 'atcoder' or c in 'atcoder' and d == '@'):
        print('You will lose')
        exit()
print('You can win')