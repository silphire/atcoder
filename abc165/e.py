n, m = map(int, input().split())

def out(s, e):
    while s < e:
        print("{} {}".format(s, e))
        s += 1
        e -= 1

odd = m % 2
out(1, m + odd)
out(m + 1 + odd, 2 * m + 1)