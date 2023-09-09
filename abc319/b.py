n = int(input())
s = ''
for i in range(n + 1):
    c = '-'
    for j in range(1, 10):
        if n % j == 0 and i % (n // j) == 0:
            c = str(j)
            break
    s += c
print(s)