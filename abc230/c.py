n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())

for x in range(p, q + 1):
    t = ''
    for y in range(r, s + 1):
        if x - y == a - b or x + y == a + b:
            t += '#'
        else:
            t += '.'
    print(t)