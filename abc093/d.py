a, b = map(int, input().split())

a -= 1
b -= 1

ans = []
for y in range(25):
    s = ''
    for x in range(50):
        if b > 0:
            s += '#.'
            b -= 1
        else:
            s += '..'
    ans.append(s)
    ans.append('.' * 100)

for y in range(25):
    s = ''
    for x in range(50):
        if a > 0:
            s += '#.'
            a -= 1
        else:
            s += '##'
    ans.append('#' * 100)
    ans.append(s)

print('100 100')
print('\n'.join(ans))