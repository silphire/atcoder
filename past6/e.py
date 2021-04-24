from collections import deque

n = int(input())
s = input().rstrip()

a = deque()
for i in range(n):
    x = i + 1
    if s[i] == 'L':
        a.appendleft(x)
    elif s[i] == 'R':
        a.append(x)
    elif s[i] == 'A':
        if len(a) <= 0:
            print('ERROR')
        else:
            print(a.popleft())
    elif s[i] == 'B':
        if len(a) <= 1:
            print('ERROR')
        else:
            y = a.popleft()
            print(a.popleft())
            a.appendleft(y)
    elif s[i] == 'C':
        if len(a) <= 2:
            print('ERROR')
        else:
            y1 = a.popleft()
            y2 = a.popleft()
            print(a.popleft())
            a.appendleft(y2)
            a.appendleft(y1)
    elif s[i] == 'D':
        if len(a) <= 0:
            print('ERROR')
        else:
            print(a.pop())
    elif s[i] == 'E':
        if len(a) <= 1:
            print('ERROR')
        else:
            y = a.pop()
            print(a.pop())
            a.append(y)
    else:
        if len(a) <= 2:
            print('ERROR')
        else:
            y1 = a.pop()
            y2 = a.pop()
            print(a.pop())
            a.append(y2)
            a.append(y1)