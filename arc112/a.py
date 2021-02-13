def s(x):
    return x * (x + 1) // 2

for _ in range(int(input())):
    l, r = map(int, input().split())
    if l * 2 > r:
        print(0)
    elif l == r:
        print(int(l == 0))
    else:
        print(s(r - l - (l - 1)))
