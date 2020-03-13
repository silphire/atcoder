n = list(map(int, list(input().rstrip())))
x = 0
y = 0
for i in range(len(n)):
    if i % 2 == 0:
        x += n[-i - 1]
    else:
        y += n[-i - 1]
print((x - y) % 11)
