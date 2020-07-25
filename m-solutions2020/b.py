a, b, c = map(int, input().split())
k = int(input())

while a >= b:
    k -= 1
    b *= 2
while b >= c:
    k -= 1
    c *= 2
if k >= 0:
    print('Yes')
else:
    print('No')