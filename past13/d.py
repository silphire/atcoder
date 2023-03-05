n, m = map(int, input().split())
s = input().rstrip()

aa = [0] * n
x = 0
i = 0
for c in s:
    aa[i] += 1
    if c == '+':
        aa[i] += x
        x = 0
    elif c == '-':
        x += aa[i]
        aa[i] = 0
    i = (i + 1) % n
for a in aa:
    print(a)