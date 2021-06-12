n = int(input()) % 30

x = [x for x in range(1, 7)]

for i in range(n):
    x[i % 5], x[i % 5 + 1] = x[i % 5 + 1], x[i % 5]
print(''.join(map(str, x)))