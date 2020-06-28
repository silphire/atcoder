d = int(input())
c = tuple(map(int, input().split()))
s = [
    tuple(map(int, input().split()))
    for _ in range(d)
]

m = 0
ans = []
last = [0] * 26
for i in range(d):
    # for all contest
    mdmax = -10000000000000000
    mdi = 0
    for j, ss in enumerate(s[i]):
        md = 0
        # choose one contest to open
        for k in range(26):
            if j == k:
                md += ss
            else:
                md -= (i + 1 - last[k]) * c[k]
        if md > mdmax:
            mdi = j
            mdmax = md

    ans.append(mdi + 1)
    m += mdmax

    last[mdi] = i + 1

for a in ans:
    print(a)
print(m)