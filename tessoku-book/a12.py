n, k = map(int, input().split())
aa = list(map(int, input().split()))

l = 0
r = 10 ** 9
while r - l > 1:
    x = (l + r) // 2
    y = 0
    for a in aa:
        y += x // a
    if y > k:
        r = x
    elif y < k:
        l = x
    else:
        print(x)
        exit()
print(r)