s = input().rstrip()
c = (sum(map(int, s[1:-1:2])) + 3 * sum(map(int, s[:-1:2]))) % 10
if c == int(s[-1]):
    print('Yes')
else:
    print('No')