n = int(input())
aa = list(map(int, input().split()))

def decode(x):
    global n
    a = []
    for i in range(n):
        if x & (1 << i) != 0:
            a.append(str(i + 1))
    return f'{len(a)} {" ".join(a)}'

d = [None] * 200
for x in range(1, 2 ** n):
    t = 0
    for i in range(n):
        if x & (1 << i) != 0:
            t += aa[i]
    t %= 200
    if d[t] is None:
        d[t] = x
    else:
        print('Yes')
        print(decode(d[t]))
        print(decode(x))
        exit()
print('No')