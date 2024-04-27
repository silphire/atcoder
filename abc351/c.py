from collections import deque

n = int(input())
aa = list(map(int, input().split()))

bb = deque()
for a in aa:
    bb.append(a)
    while True:
        if len(bb) <= 1:
            break
        x = bb.pop()
        y = bb.pop()
        if x == y:
            bb.append(x + 1)
        else:
            bb.append(y)
            bb.append(x)
            break

print(len(bb))