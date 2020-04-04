k = int(input())


def make_runrun(n, depth):
    r = [n]
    if depth == 0:
        return r
    x = n % 10

    if x >= 1:
        r.extend(make_runrun(n * 10 + x - 1, depth - 1))
    r.extend(make_runrun(n * 10 + x, depth - 1))
    if x < 9:
        r.extend(make_runrun(n * 10 + x + 1, depth - 1))
    
    return r

r = []
for i in range(1, 10):
    r.extend(make_runrun(i, 10))
r = sorted(r)
print(r[k - 1])
