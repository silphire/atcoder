s = input().rstrip()
l, r = map(int, input().split())
if s == str(int(s)) and l <= int(s) <= r:
    print('Yes')
else:
    print('No')