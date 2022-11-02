from collections import deque

n = int(input())
aa = deque(sorted(map(int, input().split())))

x = 0
while len(aa) > 1:
    b = aa.pop()
    r = b % aa[0]
    if r > 0:
        aa.appendleft(r)
    x += 1
print(x)