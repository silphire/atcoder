x, n = map(int, input().split())
ps = set(map(int, input().split()))

i = 0
while True:
    if (x - i) not in ps:
        print(x - i)
        exit(0)
    if (x + i) not in ps:
        print(x + i)
        exit(0)
    i += 1