k = int(input())
x = []
while k > 0:
    x.append(2 * (k & 1))
    k >>= 1
print(''.join(map(str, x[::-1])))