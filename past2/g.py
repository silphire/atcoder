from collections import defaultdict

nq = int(input())

i = 0
s = []
for _ in range(nq):
    q = input().rstrip().split()
    if q[0] == '1':
        c = q[1]
        x = int(q[2])
        if len(s) > 0 and s[-1][0] == c and i < len(s):
            s[-1][1] += x
        else:
            s.append([c, x])
    else:
        d = int(q[1])
        ctr = defaultdict(int)
        while d > 0 and i < len(s):
            nd = min(d, s[i][1])
            ctr[s[i][0]] += nd

            d -= nd
            s[i][1] -= nd
            
            if s[i][1] == 0:
                i += 1
        print(sum(map(lambda x: int(x) * int(x), ctr.values())))