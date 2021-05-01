from collections import deque

s = input().rstrip()
t = deque()
f = True
for c in s:
    if c == 'R':
        f = not f
    else:
        if f:
            if len(t) == 0 or t[-1] != c:
                t.append(c)
            else:
                t.pop()
        else:
            if len(t) == 0 or t[0] != c:
                t.appendleft(c)
            else:
                t.popleft()
if f:
    t = ''.join(t)
else:
    t = ''.join(reversed(t))
print(t)