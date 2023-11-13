from collections import deque
s = input()
q = deque(list(s))

ans = 0
while q:
    if q[0] == q[-1]:
        q.popleft()
        if len(q) > 1:
            q.pop()
    else:
        if q[0] == 'x':
            q.append('x')
        elif q[-1] == 'x':
            q.appendleft('x')
        else:
            print(-1)
            exit()
        ans += 1
print(ans)
