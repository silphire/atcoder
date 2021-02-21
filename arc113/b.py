a, b, c = map(int, input().split())

x = a % 10
xx = 1
pp = []
while True:
    xx *= x
    r = xx % 10
    if pp and pp[0] == r:
        break
    pp.append(r)

print(pow(a, pow(b, c, len(pp)) + len(pp), 10))