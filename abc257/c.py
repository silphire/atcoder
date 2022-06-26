import bisect

n = int(input())
s = input().rstrip()
ww = list(map(int, input().split()))

wa = sorted([ww[i] for i in range(n) if s[i] == '1'])
wc = sorted([ww[i] for i in range(n) if s[i] == '0'])
na = len(wa)
nc = len(wc)

ma = 0
for w in ww + [float('-inf'), float('inf')]:
    ca = na - bisect.bisect_left(wa, w) 
    cc = bisect.bisect_left(wc, w)
    ma = max(ma, ca + cc)
print(ma)
