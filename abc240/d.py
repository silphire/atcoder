from collections import deque

n = int(input())
aa = list(map(int, input().split()))

ans = deque()
nq = 0
for a in aa:
    if not ans:
        if a != 1:
            ans.append((a, 1))
            nq += 1
    else:
        b, m = ans.pop()
        if a == b:
            m += 1
            nq += 1
            if a != m:
                ans.append((a, m))
            else:
                nq -= m
        else:
            ans.append((b, m))
            if a != 1:
                ans.append((a, 1))
                nq += 1
    print(nq)