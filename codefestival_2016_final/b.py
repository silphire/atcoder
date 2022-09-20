n = int(input())

l = 1
r = 10 ** 4
while r - l > 1:
    x = (l + r) // 2
    s = x * (x + 1) // 2
    if s == x:
        for i in range(x):
            print(i + 1)
        exit()
    elif s < n:
        l = x
    else:
        r = x
t = [a for a in range(x + 1, 0, -1)]
st = (x + 1) * (x + 2) // 2
for i, a in enumerate(t):
    if st == n:
        break
    elif st - n >= a:
        t[i] = 0
        st -= a
for a in t:
    if a > 0:
        print(a)