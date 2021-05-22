d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
print(''.join(map(lambda c: d[c], reversed(list(input().rstrip())))))
