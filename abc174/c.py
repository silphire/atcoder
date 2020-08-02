k = int(input())

r = set()
x = 7
i = 1
while True:
    rr = x % k
    if rr == 0:
        print(i)
        break
    if rr in r:
        print(-1)
        break
    x = (x * 10 + 7) % k
    i += 1
    r.add(rr)