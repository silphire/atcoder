n, m = map(int, input().split())
ss = list(input().rstrip().split())
tt = set(input().rstrip().split())

for s in ss:
    if s in tt:
        print('Yes')
    else:
        print('No')