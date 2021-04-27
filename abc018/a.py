x = sorted([
    (-int(input()), x)
    for x in range(3)
])
x = sorted([
    (a, i + 1)
    for i, (b, a) in enumerate(x)
])
for a, b in x:
    print(b)