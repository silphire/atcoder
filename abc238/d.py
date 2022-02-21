t = int(input())
for _ in range(t):
    a, s = map(int, input().split())
    x = s - 2 * a
    if x >= 0 and x & a == 0:
        print('Yes')
    else:
        print('No')