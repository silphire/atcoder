n, m, q = map(int, input().split())
p = [[] for _ in range(n)]
solved = [0] * m
for i in range(q):
    s = tuple(map(int, input().split()))
    if s[0] == 1:
        x = 0
        for i in p[s[1] - 1]:
            x += n - solved[i]
        print(x)
    else:
        nn = s[1] - 1
        mm = s[2] - 1
        solved[mm] += 1
        p[nn].append(mm)
