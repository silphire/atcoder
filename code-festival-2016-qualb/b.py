n, a, b = map(int, input().split())
s = input().rstrip()

nd = 0
nf = 0
for c in s:
    if c == 'a':
        if nd < a + b:
            print('Yes')
            nd += 1
        else:
            print('No')
    elif c == 'b':
        if nd < a + b and nf < b:
            print('Yes')
            nd += 1
            nf += 1
        else:
            print('No')
    else:
        print('No')