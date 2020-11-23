s, p = map(int, input().split())

for n in range(1, int(p ** 0.5) + 2):
    if p % n == 0:
        m = p // n
        if n + m == s:
            print('Yes')
            exit()
print('No')