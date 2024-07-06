from collections import deque

n = int(input())
s = input()
t = input()
visited = set()

def encode(a: str) -> int:
    x = 0
    for c in a:
        x *= 4
        if c == 'B':
            x += 1
        elif c == 'W':
            x += 2
    return x * 16

xs = encode(s)
xt = encode(t)

q = deque([(xs, 0)])
while q:
    x, xn = q.popleft()
    if x == xt:
        print(xn)
        exit()
    if x in visited:
        continue
    visited.add(x)

    aa = [0] * (n + 2)
    p = 0
    for i in range(n + 2):
        a = (x >> (i * 2)) & 3
        if a == 0:
            p = n + 2 - i - 1
        aa[-i - 1] = a
    # print(aa, xn)

    for i in range(n + 2 - 1):
        if abs(p - i) <= 1:
            continue
        nx = 0
        for j in range(n + 2):
            nx *= 4
            if j == p:
                nx += aa[i]
            elif j == p + 1:
                nx += aa[i + 1]
            elif j == i or j == i + 1:
                continue
            else:
                nx += aa[j]
        if nx in visited:
            continue
        if nx == xt:
            print(xn + 1)
            exit()
        q.append((nx, xn + 1))
            
print(-1)