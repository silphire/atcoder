from collections import defaultdict

d = defaultdict(int)
q = int(input())
for _ in range(q):
    qq = list(map(int, input().split()))
    if qq[0] == 1:
        d[qq[1]] += 1
    elif qq[0] == 2:
        d[qq[1]] -= 1
        if d[qq[1]] == 0:
            del d[qq[1]]
    else:
        print(len(d))