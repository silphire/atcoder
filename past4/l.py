from collections import defaultdict

n, q = map(int, input().split())
hh = list(map(int, input().split()))

hdiff = 0
hdic = defaultdict(int)
for i in range(0, n, 2):
    if i > 0:
        hdic[hh[i] - hh[i - 1]] += 1
    if i < n - 1:
        hdic[hh[i] - hh[i + 1]] += 1

for _ in range(q):
    qq = list(map(int, input().split()))
    if qq[0] == 3:
        p = qq[1] - 1
        t = qq[2]
        if p % 2 == 0:
            if p > 0:
                hdic[hh[p] - hh[p - 1]] -= 1
            if p < n - 1:
                hdic[hh[p] - hh[p + 1]] -= 1
            hh[p] += t
            if p > 0:
                hdic[hh[p] - hh[p - 1]] += 1
            if p < n - 1:
                hdic[hh[p] - hh[p + 1]] += 1
        else:
            if p > 0:
                hdic[hh[p - 1] - hh[p]] -= 1
            if p < n - 1:
                hdic[hh[p + 1] - hh[p]] -= 1
            hh[p] += t
            if p > 0:
                hdic[hh[p - 1] - hh[p]] += 1
            if p < n - 1:
                hdic[hh[p + 1] - hh[p]] += 1
    elif qq[0] == 1:
        hdiff -= qq[1]
    else:
        hdiff += qq[1]

    print(hdic.get(hdiff, 0))
