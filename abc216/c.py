n = int(input())
s = ''
while n > 0:
    if n & 1 == 1:
        s += 'A'
        n -= 1
    if n == 0:
        break
    n //= 2
    s += 'B'
print(''.join(reversed(s)))
