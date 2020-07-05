from collections import Counter
n = int(input())
s = [None] * n
for i in range(n):
    s[i] = input().rstrip()
c = Counter(s)
for x in ['AC', 'WA', 'TLE', 'RE']:
    print('{} x {}'.format(x, c[x]))
