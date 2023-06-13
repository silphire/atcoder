n, k = map(int, input().split())
aa = list(map(int, input().split()))

def cand(arr):
    na = len(arr)
    r = set()
    for i in range(1 << na):
        x = i
        y = 0
        for j in range(na):
            if (x >> j) & 1 == 1:
                y += arr[j]
        r.add(y)
    return r

f = cand(aa[:n // 2])
b = cand(aa[n // 2:])

for a in f:
    if (k - a) in b:
        print('Yes')
        exit()
print('No')