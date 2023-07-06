from collections import deque

n, x = map(int, input().split())
aa = list(input())

q = deque([x - 1])
aa[x - 1] = '@'
while q:
    p = q.popleft()
    if p - 1 >= 0 and aa[p - 1] == '.':
        aa[p - 1] = '@'
        q.append(p - 1)
    if p + 1 < n and aa[p + 1] == '.':
        aa[p + 1] = '@'
        q.append(p + 1)

print(''.join(aa))